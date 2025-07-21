import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.metrics import Precision, Recall, AUC
from tensorflow.keras.optimizers import Adam
from sklearn.utils.class_weight import compute_class_weight
from tensorflow.keras.initializers import HeNormal
from tensorflow.keras.regularizers import l2
from tensorflow.keras.callbacks import Callback

import numpy

class MetricError(Exception):
    """Exception raised for errors that occur due to metric calculation."""
    pass

class LossNaNError(Exception):
    """Exception raised when the loss becomes NaN or infinite."""
    pass

class LossIncreaseError(Exception):
    """Exception raised when the loss increases for a defined number of consecutive epochs."""
    pass

class LossStagnationError(Exception):
    """Exception raised when the loss stagnates for a defined number of consecutive epochs."""
    pass


class F1Score(tf.keras.metrics.Metric):
    def __init__(self, name='f1_score', **kwargs):
        super(F1Score, self).__init__(name=name, **kwargs)
        self.precision = tf.keras.metrics.Precision()
        self.recall = tf.keras.metrics.Recall()

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.round(y_pred)
        self.precision.update_state(y_true, y_pred, sample_weight)
        self.recall.update_state(y_true, y_pred, sample_weight)

    def result(self):
        p = self.precision.result()
        r = self.recall.result()
        # print(f"Precision: {p}, Recall: {r}")  # Adicione logs para depuração
        return tf.cond(
            tf.equal(p + r, 0),
            lambda: tf.constant(0.0),
            lambda: 2 * (p * r) / (p + r)
        )

    def reset_state(self):
        self.precision.reset_state()
        self.recall.reset_state()

class StopTrainingOnZeroF1Score(Callback):
    def __init__(self):
        super(StopTrainingOnZeroF1Score, self).__init__()
        self.zeros = 0

    def on_epoch_end(self, epoch, logs=None):
        # Verify if the logs are available
        f1_score = logs.get('f1_score', 0)  # Default to 0 if not found
        val_f1_score = logs.get('val_f1_score', 0)  # Default to 0 if not found

        # Increment the counter if both are zero
        if f1_score == 0 and val_f1_score == 0:
            self.zeros += 1
        else:
            self.zeros = 0

        # Interrompe o treinamento e lança uma exceção se houver dois zeros consecutivos
        if self.zeros >= 2:
            print(f"Terminating training at epoch {epoch + 1}.")
            self.model.stop_training = True
            raise MetricError("Metric Error: training terminated due to zero F1 score for 2 consecutive epochs.")
        

class StopTrainingForLossIssues(Callback):
    def __init__(self):
        super(StopTrainingForLossIssues, self).__init__()
        self.last_loss = None
        self.stagned_loss_count = 0
        self.stagned_loss_limit = 3
        self.increasing_loss_count = 0
        self.increasing_loss_limit = 5

    def on_epoch_end(self, epoch, logs=None):
        loss = logs.get('loss')
        if loss is None:
            return
        
        # Check for NaN or infinite loss
        if numpy.isnan(loss) or numpy.isinf(loss):
            print(f"Terminating training at epoch {epoch + 1}.")
            self.model.stop_training = True
            raise LossNaNError(f'LossNaNError: terminating training due to NaN or inf loss.')

        # Check if the loss is the same as the last epoch
        if self.last_loss is not None and self.last_loss == loss:
            self.stagned_loss_count += 1
        else:
            self.stagned_loss_count = 0

        # Check if the loss is increasing
        if self.last_loss is not None and loss > self.last_loss:
            self.increasing_loss_count += 1
        else:
            self.increasing_loss_count = 0

        # Interrupt training if the loss has increased for five consecutive epochs
        if self.increasing_loss_count >= self.increasing_loss_limit:
            print(f"Terminating training at epoch {epoch + 1}.")
            self.model.stop_training = True
            raise LossIncreaseError("LossIncreaseError: loss increased for consecutive epochs.")

        # Interrupt training if the loss is the same for three consecutive epochs
        if self.stagned_loss_count >= self.stagned_loss_limit:
            print(f"Terminating training at epoch {epoch + 1}.")
            self.model.stop_training = True
            raise LossStagnationError("LossStagnationError: loss stagnated for consecutive epochs.")

        # Update the last loss
        self.last_loss = loss


class LSTMModel:
    def __init__(self, window_size, metrics=None, class_weights=None, debug=False, learning_rate=0.01, optimizer=None):
        self.window_size = window_size
        self.metrics = metrics
        self.class_weights = class_weights if class_weights is not None and len(class_weights) > 0 else {0: 0.5, 1: 0.5}
        self.debug = debug
        self.model = self.build_model(learning_rate, optimizer)
        self.best_epoch = None

        # Verifica a versão do TensorFlow
        self.tf_version = tf.__version__
        # Verifica se a versão é igual ou superior a 2.12
        if self.tf_version >= "2.12":
            # Altera a extensão para .keras
            self.file_model_extension = ".keras"
        else:
            self.file_model_extension = ".h5"
        

    def setup_callbacks(self, model_name, save_best_only=True):
        if self.debug:
            print("Setting up callbacks...")
        return [
            EarlyStopping(monitor='loss', mode='min', patience=8, restore_best_weights=False),
            EarlyStopping(monitor='val_f1_score', mode='max', patience=12, restore_best_weights=True),
            ModelCheckpoint(f"{model_name}_epoch_{{epoch:02d}}{self.file_model_extension}", monitor='val_f1_score', save_best_only=save_best_only, mode='max', verbose=1),
            ReduceLROnPlateau(monitor='val_f1_score', factor=0.1, patience=5, min_lr=0.0001),
            StopTrainingOnZeroF1Score(),
            StopTrainingForLossIssues()
        ]
    
    # Usar isso somene se você souber o que está fazendo!!!!!
    def balanced_batch_generator(self, data, labels, batch_size=32, equilibrium=0.5):
        if self.debug:
            print("Generating batches...")
        class_1_indices = numpy.where(labels == 1)[0]
        class_0_indices = numpy.where(labels == 0)[0]

        while True:
            numpy.random.shuffle(class_1_indices)
            numpy.random.shuffle(class_0_indices)

            class_1_count = int(batch_size * equilibrium)
            class_0_count = batch_size - class_1_count

            batch_indices_1 = []
            batch_indices_0 = []

            for start_idx in range(0, max(len(class_1_indices), len(class_0_indices)), batch_size):
                end_idx_1 = min(start_idx + class_1_count, len(class_1_indices))
                batch_indices_1.extend(class_1_indices[start_idx:end_idx_1])
                if len(batch_indices_1) < class_1_count:  # Se não temos dados suficientes, repetimos desde o início
                    batch_indices_1.extend(class_1_indices[:(class_1_count - len(batch_indices_1))])

                start_idx_0 = start_idx % len(class_0_indices)
                end_idx_0 = start_idx_0 + class_0_count
                if end_idx_0 > len(class_0_indices):
                    end_idx_0 -= len(class_0_indices)
                    batch_indices_0.extend(class_0_indices[start_idx_0:])
                    batch_indices_0.extend(class_0_indices[:end_idx_0])
                else:
                    batch_indices_0.extend(class_0_indices[start_idx_0:end_idx_0])

                if len(batch_indices_0) < class_0_count:  # Se não temos dados suficientes, repetimos desde o início
                    batch_indices_0.extend(class_0_indices[:(class_0_count - len(batch_indices_0))])

                if len(batch_indices_1) >= class_1_count and len(batch_indices_0) >= class_0_count:
                    break

            batch_indices = numpy.concatenate([batch_indices_1, batch_indices_0])
            numpy.random.shuffle(batch_indices)

            yield data[batch_indices], labels[batch_indices]
    
    # Recomendo fortemente criar a sua própria função de preparação de dataset ou 
    # usar a função balanced_batch_generator somente se você souber o que está fazendo.
    def prepare_dataset(self, data, labels, batch_size, class_weights):

        normalized_class_weights = {k: v / sum(class_weights.values()) for k, v in class_weights.items()}
        dataset = tf.data.Dataset.from_generator(
            lambda: self.balanced_batch_generator(data, labels, batch_size, equilibrium=normalized_class_weights[0]),
            output_types=(tf.float32, tf.int32),
            output_shapes=((batch_size, data.shape[1], 1), (batch_size,))
        )
        if self.debug:
            # print normalized class weights values per class
            print("Normalized class weights: ", normalized_class_weights)
            print("Configuring shuffle and prefetch...")
        dataset = dataset.shuffle(buffer_size=10000).prefetch(tf.data.experimental.AUTOTUNE)
        return dataset

    def build_model(self, learning_rate=0.01, optimizer=None):
        if self.debug:
            print("Build model...")
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=(self.window_size, 1)),
            tf.keras.layers.LSTM(64, return_sequences=True, kernel_initializer=HeNormal()),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.LSTM(64, kernel_initializer=HeNormal(), kernel_regularizer=l2(0.01)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dense(64, activation='relu', kernel_initializer=HeNormal(), kernel_regularizer=l2(0.01)),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        if optimizer is None:
            optimizer = Adam(learning_rate=learning_rate)
        model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=self.metrics if self.metrics is not None else ['accuracy'])
        return model
    
    def train(self, train_data, train_labels, val_data, val_labels, epochs=100, batch_size=32, weight_factor=1, model_name="model", save_best_only=True):
        
        class_weights_dict = {0: self.class_weights[0], 1: self.class_weights[1] / weight_factor}
        # Implementar a ssua própria função de preparação de dataset ou usar a balanced_batch_generator somente se você souber o que está fazendo.
        #train_dataset = self.prepare_dataset(train_data, train_labels, batch_size, class_weights_dict)

        model_name = f"{model_name}/model_"

        callbacks = self.setup_callbacks(model_name=model_name, save_best_only=save_best_only)
        steps_per_epoch = len(train_data) // batch_size

        if self.debug:
            print(f"Starting training: steps per epoch = {steps_per_epoch}, batch size = {batch_size}")
            print(f"Mixed model name: {model_name}")

        if self.tf_version <= "2.10.0":
            history = self.model.fit(
                train_dataset, steps_per_epoch=steps_per_epoch, epochs=epochs, class_weight=class_weights_dict,  # Aplicar pesos das classes
                validation_data=(val_data, val_labels), callbacks=callbacks, use_multiprocessing=True, verbose=1  # Explicitamente definindo verbose como 1
            )
        else:
            history = self.model.fit(
                train_dataset, steps_per_epoch=steps_per_epoch, epochs=epochs, class_weight=class_weights_dict,  
                validation_data=(val_data, val_labels), callbacks=callbacks, verbose=1  
        )

        return history
    
    def plot_metrics(self, history, metrics=['loss', 'accuracy'], save_path=None):
        num_metrics = len(metrics)
        plt.figure(figsize=(6 * num_metrics, 6))  # Ajusta a largura da figura baseada no número de métricas

        for i, metric in enumerate(metrics):
            plt.subplot(1, num_metrics, i+1)
            train_metric = history.history.get(metric, [])
            val_metric = history.history.get(f'val_{metric}', [])
            if train_metric:  # Verifica se a métrica possui valores para evitar gráficos vazios
                plt.plot(train_metric, label=f'Training {metric.capitalize()}')
            if val_metric:
                plt.plot(val_metric, label=f'Validation {metric.capitalize()}')
            plt.xlabel('Epoch')
            plt.ylabel(metric.capitalize())
            plt.title(f'Training and Validation {metric.capitalize()}')
            plt.legend()

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        plt.show()

    #def predict(self, test_data, batch_size=32):
    #    #test_data_expanded = numpy.expand_dims(test_data, -1)
    #    if self.debug:
    #        print(test_data.shape)
    #    return self.model.predict(test_data, batch_size=batch_size)

    def save_model(self, model_name):
        tf.saved_model.save(self.model, model_name)
            
    def load_model(self, path, custom_objects=None):
        self.model = tf.keras.models.load_model(path, custom_objects=custom_objects)