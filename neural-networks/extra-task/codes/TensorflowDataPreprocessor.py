import numpy
import pandas
from sklearn.utils.class_weight import compute_class_weight
import pkg_resources

class TensorflowDataPreprocessor:
    def __init__(self, XTrain, XValidation, XTest, debug=False):
        self.XTrain = XTrain.astype(float)
        self.XValidation = XValidation.astype(float)
        self.XTest = XTest.astype(float)
        self.debug = debug
        self.rename_columns()

    def rename_columns(self):
        self.XTrain.columns = [f"feature_{i}" for i in range(self.XTrain.shape[1])]
        self.XValidation.columns = self.XTrain.columns
        self.XTest.columns = self.XTrain.columns
        if self.debug:
            print("Renamed columns:")
            print(self.XTrain.columns)

    def normalize_data(self):
        all_data = pandas.concat([self.XTrain, self.XValidation, self.XTest], ignore_index=True)
        if self.debug:
            print("Concatenated data for normalization:")
            display(all_data.describe())
        
        for col in all_data.columns:
            min_val = all_data[col].min()
            max_val = all_data[col].max()
            self.XTrain[col] = (self.XTrain[col] - min_val) / (max_val - min_val)
            self.XValidation[col] = (self.XValidation[col] - min_val) / (max_val - min_val)
            self.XTest[col] = (self.XTest[col] - min_val) / (max_val - min_val)
            
        if self.debug:
            print("Data after normalization:")
            print("XTrain:")
            display(self.XTrain.describe())
            print("XValidation:")
            display(self.XValidation.describe())
            print("XTest:")
            display(self.XTest.describe())

    def prepare_data(self, yTrain, yValidation, yTest, number_of_samples=-1, number_of_samples_validation=-1):
        yTrain = yTrain[:number_of_samples].reset_index(drop=True)
        yValidation = yValidation[:number_of_samples_validation].reset_index(drop=True)
        yTest = yTest[:number_of_samples_validation].reset_index(drop=True)

        XTrain = self.XTrain[:number_of_samples].values
        XValidation = self.XValidation[:number_of_samples_validation].values
        XTest = self.XTest[:number_of_samples_validation].values

        XTrain = numpy.expand_dims(XTrain, -1)
        XValidation = numpy.expand_dims(XValidation, -1)
        XTest = numpy.expand_dims(XTest, -1)

        if self.debug:
            print("Shapes after preparing for LSTM:")
            print(f"XTrain shape: {XTrain.shape}, yTrain shape: {yTrain.shape}")
            print(f"XValidation shape: {XValidation.shape}, yValidation shape: {yValidation.shape}")
            print(f"XTest shape: {XTest.shape}, yTest shape: {yTest.shape}")

        return XTrain, yTrain, XValidation, yValidation, XTest, yTest

    def compute_weights(self, yTrain):

        # Verifica a versão do sklearn
        sklearn_version = pkg_resources.get_distribution("scikit-learn").version
        if self.debug:
            print(f"Scikit-learn version: {sklearn_version}")
        
        # Define as classes baseado na versão do sklearn
        if sklearn_version < '0.24':  # Exemplo de versão, ajuste conforme necessário
            classes = [0, 1]
        else:
            classes = numpy.array([0, 1])

        weights = compute_class_weight('balanced', classes=numpy.unique(yTrain), y=yTrain)
        if self.debug:
            print("Computed class weights:")
            print(weights)
            print(f"Class: {numpy.unique(yTrain)}")
        return weights

    def check_nans(self, X, y):
        if numpy.isnan(X).any() or numpy.isnan(y).any():
            print("NaNs found in data")
            # Implement more specific handling here if needed.