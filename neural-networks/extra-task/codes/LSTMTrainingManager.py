import os
import pandas
from tensorflow.keras.metrics import Precision, Recall
from Classes.LSTM import LSTMModel, F1Score
from tensorflow.keras.optimizers import Adam
from Classes.ModelEvaluator import ModelEvaluator
from Classes.ModelMetricsManager import ModelMetricsManager

STEP_SIZE = 'stepSize'

PRECISION = 'Precision'
RECALL = 'Recall'
F1_SCORE = 'F1-Score'
THRESHOLD = 'Threshold'
AUROC = 'AUROC'
AUPRC = 'AUPRC'
TRAIN = 'Train'
VALIDATION = 'Validation'
TEST = 'Test'
WINDOWSIZE = 'WindowSize'
DATASET_TYPE = 'DatasetType'

class LSTMTrainingManager:
    def __init__(self, experiment_directory, experiment_id, debug=False):
        self.experiment_directory = experiment_directory
        self.experiment_id = experiment_id
        self.results_df = pandas.DataFrame(columns=[
            'epoch', 'batch_size', 'factor', 'train_loss', 'train_precision', 'train_recall', 'train_f1_score',
            'val_loss', 'val_precision', 'val_recall', 'val_f1_score'
        ])
        self.className = "LSTMTrainingManager"
        self.debug = debug
        self.model_csv_file_path_class_0 = f'{experiment_directory}/model_metrics_classe_0.csv'
        self.model_csv_file_path_class_1 = f'{experiment_directory}/model_metrics_classe_1.csv'

        self.model_metrics_manager_class_0 = ModelMetricsManager(self.model_csv_file_path_class_0)
        self.model_metrics_manager_class_1 = ModelMetricsManager(self.model_csv_file_path_class_1)
        self.lstm = None

    def setup_data(self, XTrain, yTrain, XValidation, yValidation, XTest, yTest):
        self.XTrain = XTrain
        self.yTrain = yTrain
        self.XValidation = XValidation
        self.yValidation = yValidation
        self.XTest = XTest
        self.yTest = yTest

    def buid_default_model(self, window_size, metrics, class_weights, debug, learning_rate=0.01, optimizer=None):

        if optimizer is None:
            optimizer = Adam(learning_rate=learning_rate)  # Default optimizer

        model = LSTMModel(
            window_size=window_size,
            metrics=metrics,
            class_weights=class_weights,
            debug=debug,
            optimizer=optimizer # Pass the optimizer to the model
        )
        return model

    def setup_model(self, model=None, learning_rate=0.01, class_weights={0: 0.5, 1: 0.5}, optimizer=None):
        self.class_weights = class_weights
        if(model is None):
            metrics = [Precision(name='precision'), Recall(name='recall'), F1Score()]
            self.lstm = self.buid_default_model(self.XTrain.shape[1], metrics, self.class_weights, self.debug, learning_rate, optimizer)
        else:
            self.lstm = model
            
    def train_model(self, batch_size, factor, epochs=3, save_best_only=False):

        if not self.lstm:
            raise Exception("Model not configured. Please call setup_model first.")

        self.batch_size = batch_size
        self.factor = factor

        print(f"{self.className}: Training model with batch_size={batch_size} and factor={factor} for experiment ID={self.experiment_id}...")

        try:
            self.history = self.lstm.train(self.XTrain, self.yTrain,
                self.XValidation, self.yValidation,
                epochs=epochs,
                batch_size=batch_size,
                weight_factor=factor,
                model_name=self.experiment_directory,
                save_best_only=save_best_only
            )
            # Salvar curvas de aprendizado
            print(f"{self.className}: Saving training curves for batch_size={batch_size} and factor={factor}...")
            training_curves_path = os.path.join(self.experiment_directory, f"training_curves_{batch_size}_{factor}.png")
            self.lstm.plot_metrics(self.history, metrics=['loss', 'precision', 'recall', 'f1_score'], save_path=training_curves_path)

            # Log training results
            self.log_training_results()
            
            # return the results dataframe
            return self.results_df
            
        except Exception as e:
            print(f"Error during training model.")
            raise  # Re-raise the exception to be caught by ExperimentManager

    def evaluate_model(self, directoryPath=None):

        # Predictions for data sets
        trainProbabilities = self.lstm.model.predict(self.XTrain, batch_size=self.batch_size)
        validationProbabilities = self.lstm.model.predict(self.XValidation, batch_size=self.batch_size)
        testProbabilities = self.lstm.model.predict(self.XTest, batch_size=self.batch_size)

        # show trainProbabilities
        #print(trainProbabilities[:20])
        # show labels
        #print(self.yTrain[:20])

        if directoryPath is None:
            directoryPath = self.experiment_directory

        try:
            # Evaluation and reports
            parameters = {'outputDir': directoryPath, DATASET_TYPE: 'TRAIN', WINDOWSIZE: self.batch_size, STEP_SIZE: self.factor}
            trainEvaluator = ModelEvaluator(trainProbabilities, self.yTrain, threshold=-1, minPrecision=0.7)
            trainEvaluator.execute()
            trainEvaluator.report(saveFigure=True, params=parameters)

            parameters[DATASET_TYPE] = 'VALIDATION'
            validationEvaluator = ModelEvaluator(validationProbabilities, self.yValidation, threshold=-1, minPrecision=0.7)
            validationEvaluator.execute()
            estimatedThreshold = validationEvaluator.getThreshold()
            validationEvaluator.report(saveFigure=True, params=parameters)

            parameters[DATASET_TYPE] = 'TEST'
            testEvaluator = ModelEvaluator(testProbabilities, self.yTest, threshold=estimatedThreshold)
            testEvaluator.execute()
            testEvaluator.report(saveFigure=True, params=parameters)

            self.model_metrics_manager_class_1.add_entry(trainEvaluator, self.batch_size, self.factor, 'Train')
            self.model_metrics_manager_class_1.add_entry(validationEvaluator, self.batch_size, self.factor, 'Validation')
            self.model_metrics_manager_class_1.add_entry(testEvaluator, self.batch_size, self.factor, 'Test')
            self.model_metrics_manager_class_1.save_metrics_to_csv()
            # Adiciona as métricas do modelo de avaliação
            #all_metrics_manager.add_dataset_metrics(windowSize, step, windowingDataFrame)

            trainEvaluator.execute(targetClass='False', threshold=estimatedThreshold)
            validationEvaluator.execute(targetClass='False', threshold=estimatedThreshold)
            testEvaluator.execute(targetClass='False', threshold=estimatedThreshold)

            self.model_metrics_manager_class_0.add_entry(trainEvaluator, self.batch_size, self.factor, 'Train')
            self.model_metrics_manager_class_0.add_entry(validationEvaluator, self.batch_size, self.factor, 'Validation')
            self.model_metrics_manager_class_0.add_entry(testEvaluator, self.batch_size, self.factor, 'Test')
            self.model_metrics_manager_class_0.save_metrics_to_csv()

            return self.model_metrics_manager_class_0.metrics_df, self.model_metrics_manager_class_1.metrics_df
        
        except Exception as e:
            print(f"Error during evaluation: {str(e)}")
            raise  # Re-raise the exception to be caught by ExperimentManager

    def log_training_results(self):
        for epoch in range(len(self.history.history['loss'])):
            new_row = pandas.DataFrame({
                'epoch': [epoch + 1],
                'batch_size': [self.batch_size],
                'factor': [self.factor],
                'train_loss': self.history.history['loss'][epoch],
                'train_precision': self.history.history['precision'][epoch],
                'train_recall': self.history.history['recall'][epoch],
                'train_f1_score': self.history.history['f1_score'][epoch],
                'val_loss': self.history.history['val_loss'][epoch],
                'val_precision': self.history.history['val_precision'][epoch],
                'val_recall': self.history.history['val_recall'][epoch],
                'val_f1_score': self.history.history['val_f1_score'][epoch]
            })
            self.results_df = pandas.concat([self.results_df, new_row], ignore_index=True)

        # Save results to CSV
        results_csv_path = os.path.join(self.experiment_directory, 'training_results.csv')
        self.results_df.to_csv(results_csv_path, index=False)
        print(f"{self.className}: Training results saved to {results_csv_path}")