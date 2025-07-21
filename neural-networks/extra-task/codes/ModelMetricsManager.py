import pandas as pandas


# Definindo constantes para as chaves
WINDOW_SIZE = 'windowSize'
WINDOW_SIZE = 'windowSize'
STEP_SIZE = 'stepSize'
PRECISION = 'Precision'
RECALL = 'Recall'
F1_SCORE = 'F1-Score'
THRESHOLD = 'Threshold'
AUROC = 'AUROC'
AUPRC = 'AUPRC'
DATASET_TYPE = 'DatasetType'

class MetricsManager:
    def __init__(self, csv_file_path=None):
        self.metrics_df = pandas.DataFrame()  # DataFrame para armazenar métricas de múltiplos avaliadores
        self.csv_file_path = csv_file_path  # Caminho para salvar o arquivo CSV

    def add_entry(self, evaluator, window_size, step_size, dataset_type):
        # Assumindo que o avaliador tenha um método que retorna as métricas em forma de dicionário
        metrics = {
            WINDOW_SIZE: window_size,
            STEP_SIZE: step_size, # Inclui o STEP_SIZE
            DATASET_TYPE: dataset_type,
            PRECISION: evaluator.metrics[PRECISION],
            RECALL: evaluator.metrics[RECALL],
            F1_SCORE: evaluator.metrics[F1_SCORE],
            AUROC: evaluator.ROCCurve[AUROC],
            AUPRC: evaluator.PRCurve[AUPRC],
            THRESHOLD: evaluator.metrics[THRESHOLD]
        }
        # Cria um DataFrame a partir do dicionário de métricas
        metrics_row = pandas.DataFrame([metrics])

        # Garante que o DataFrame temporário tenha as mesmas colunas que o DataFrame de métricas acumuladas
        if not self.metrics_df.empty:
            metrics_row = metrics_row[self.metrics_df.columns]

        # Concatena o novo DataFrame de métricas com o DataFrame acumulado
        self.metrics_df = pandas.concat([self.metrics_df, metrics_row], ignore_index=True)

    def save_metrics_to_csv(self):
        # Salva o DataFrame de métricas no arquivo CSV
        if self.csv_file_path:
            self.metrics_df.to_csv(self.csv_file_path, index=False)
            # Opcionalmente, limpa o DataFrame após salvar para evitar duplicatas na próxima execução
            #self.metrics_df = pandas.DataFrame()