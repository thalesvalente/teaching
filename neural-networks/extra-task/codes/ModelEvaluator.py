from sklearn.metrics import auc, classification_report, average_precision_score, precision_recall_curve, roc_curve
import matplotlib.pyplot as plt
import numpy
import os



# Constants
PRECISION = 'Precision'
RECALL = 'Recall'
F1_SCORE = 'F1-Score'
THRESHOLD = 'Threshold'
AUROC = 'AUROC'
AUPRC = 'AUPRC'
VALIDATION = 'Validation'
TEST = 'Test'
WINDOWSIZE = 'WindowSize'
DATASET_TYPE = 'DatasetType'
STEP_SIZE = 'stepSize'


# Class to evaluate the performance of a model
class ModelEvaluator:
    

    def __init__(self, probabilities, labels, threshold=0.5, minPrecision = 0.7, debug=False):
        '''
        Constructor

        Parameters:
            probabilities (numpy.ndarray): The predicted probabilities
            labels (numpy.ndarray): The true labels
            threshold (float): The threshold to use for classification
            minPrecision (float): The minimum acceptable precision level
            debug (bool): Whether to print debug information
        '''
        self.probabilities = probabilities
        self.labels = labels

        self.threshold = threshold
        self.estimatedThreshold = threshold        
        self.minPrecision = minPrecision

        self.metrics = None
        self.ROCCurve = None
        self.PRCurve = None

        self.debug = debug

        self.precisions = None
        self.recalls = None
        self.thresholds = None


    def findBestThreshold(self, probabilities, labels, minPrecision=-1):
        '''
        Find the threshold that maximizes the F1-Score while keeping precision above a minimum acceptable level

        Parameters:
            probabilities (numpy.ndarray): The predicted probabilities
            labels (numpy.ndarray): The true labels
            minPrecision (float): The minimum acceptable precision level

        Returns:
            float: The threshold that maximizes the F1-Score while keeping precision above the minimum acceptable
        '''

        precision, recall, thresholds = precision_recall_curve(labels, probabilities)

        # You can set a minimum acceptable precision level if needed
        bestThreshold = 0.5

        # Initialize the F1-Scores
        f1Scores = numpy.zeros_like(precision)

        # Calculate the F1-Scores only where precision + recall is not zero
        non_zero_indices = (precision + recall) != 0
        f1Scores[non_zero_indices] = 2 * precision[non_zero_indices] * recall[non_zero_indices] / (precision[non_zero_indices] + recall[non_zero_indices])
        if minPrecision > 0.5:

            # Find the threshold that maximizes recall while keeping precision above the minimum acceptable
            # Find the indices where precision is greater than or equal to the minimum acceptable
            validIndices = numpy.where(precision[:-1] >= minPrecision)[0]  # Ignore the last point which is artificially added at the end of precision and recall

            if len(validIndices) == 0:
                print("No threshold meets the minimum precision criterion.")
                maxF1ScoreIndex = numpy.argmax(f1Scores)
                bestThreshold = thresholds[maxF1ScoreIndex]
            else:

                # Find the index of the highest recall among the valid ones
                maxF1ScoreIndex = validIndices[numpy.argmax(f1Scores[validIndices])]
                bestThreshold = thresholds[maxF1ScoreIndex]

                #print(f"Best threshold to maximize F1-Score with precision >= {minPrecision}")
                #print(f"F1-Score: {f1Scores[maxF1ScoreIndex]}")
                #print(f"Recall: {recall[maxF1ScoreIndex]}")
                #print(f"Precision: {precision[maxF1ScoreIndex]}")
        else:

            bestIdx = numpy.argmax(f1Scores)
            bestThreshold = thresholds[bestIdx]
            print(f"Best threshold for F1-Score: {bestThreshold}")

        return bestThreshold


    def calculateMetrics(self, probabilities, labels, threshold, target_class='True' ):
        '''
        Calculate the evaluation metrics

        Parameters:
            probabilities (numpy.ndarray): The predicted probabilities
            labels (numpy.ndarray): The true labels
            threshold (float): The threshold to use for classification
            target_class (str): The target class

        Returns:
            dict: The evaluation metrics
        '''
        try:
            # Check for NaN in probabilities or labels before proceeding
            if numpy.any(numpy.isnan(probabilities)) or numpy.any(numpy.isnan(labels)):
                raise ValueError("ModelEvaluator > CalculateMetrics: Input contains NaN values, which are not allowed.")
            predictions = (probabilities >= threshold).astype(int)

            report = classification_report(labels, predictions, output_dict=True, zero_division=0)

            falsePositiveRates, truePositiveRates, _ = roc_curve(labels, probabilities)
            auroc = auc(falsePositiveRates, truePositiveRates)

            precisions, recalls, thresholds = precision_recall_curve(labels, probabilities)
            aupcr = average_precision_score(labels, probabilities)

            self.precisions = precisions
            self.recalls = recalls
            self.thresholds = thresholds

            metrics = {
                PRECISION: report[target_class][PRECISION.lower()],
                RECALL: report[target_class][RECALL.lower()],
                F1_SCORE: report[target_class][F1_SCORE.lower()],
                THRESHOLD: threshold
            }
            ROCCurve = {
                'falsePositiveRates': falsePositiveRates,
                'truePositiveRates': truePositiveRates,
                AUROC: auroc
            }
            PRCurve = {
                'precisions': precisions,
                'recalls': recalls,
                AUPRC: aupcr
            }

            return metrics, ROCCurve, PRCurve
        
        except ValueError as e:
            print(f"Error calculating metrics: {str(e)}")
            # You might want to handle this differently depending on your needs
            # For instance, you could return default values, or propagate the error
            raise

        except Exception as e:
            print(f"Unexpected error during metrics calculation: {str(e)}")
            raise

    
    def execute(self, targetClass='True', threshold=-1):
        '''
        Execute the evaluation

        Parameters:
            targetClass (str): The target class
            threshold (float): The threshold to use for classification
        '''

        # Find the best threshold
        if self.threshold <= 0:
            self.estimatedThreshold = self.findBestThreshold(self.probabilities, self.labels, self.minPrecision)

        # Calculate evaluation metrics
        self.metrics, self.ROCCurve, self.PRCurve = self.calculateMetrics(self.probabilities, self.labels, self.estimatedThreshold, targetClass)
    

    def printMetrics(self, metrics):
        print(f"Classification Report for threshold {metrics[THRESHOLD]:.2f}:")
        print(f"Precision: {metrics[PRECISION]:.2f}")
        print(f"Recall: {metrics[RECALL]:.2f}")
        print(f"F1-Score: {metrics[F1_SCORE]:.2f}")
        

    def plotCurve(self, xMeasurements, yMeasurements, AUC, xLabel, yLabel, title, line = None, saveFigure=False, params={}):
        '''
        Plot a curve

        Parameters:
            xMeasurements (numpy.ndarray): The x-axis values
            yMeasurements (numpy.ndarray): The y-axis values
            AUC (float): The area under the curve
            xLabel (str): The x-axis label
            yLabel (str): The y-axis label
            title (str): The title of the plot
            line (list): The line to plot
            saveFigure (bool): Whether to save the figure
            params (dict): The parameters
        '''

        plt.figure(figsize=(8, 4))
        plt.plot(xMeasurements, yMeasurements, label = title + f'(AUC = {AUC:.2f})')
        if line:
            plt.plot(line[0], line[1], linestyle='--')
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)
        plt.legend()

        if saveFigure:
            fileName = os.path.join(params['outputDir'], f"{params[DATASET_TYPE]}_{params[WINDOWSIZE]}_{params[STEP_SIZE]}_{title.replace(' ', '_')}.png")
            plt.savefig(fileName)
        plt.show()


    def report(self, saveFigure=False, params={}):
        '''
        Report the evaluation outcomes (print the evaluation metrics and plot the ROC and Precision-Recall curves)
        '''
        # Print the evaluation metrics
        self.printMetrics(self.metrics)
        
        # Plot the ROC curve
        line = [0, 1], [0, 1]
        self.plotCurve(self.ROCCurve['falsePositiveRates'], self.ROCCurve['truePositiveRates'], self.ROCCurve[AUROC], 
                       'False Positive Rate', 'True Positive Rate', 'ROC Curve', line)

        # Plot the Precision-Recall curve
        self.plotCurve(self.PRCurve['recalls'], self.PRCurve['precisions'], self.PRCurve[AUPRC], 
                       RECALL, PRECISION, 'Precision-Recall Curve', line, saveFigure, params)

        self.plotPrecisionRecallVsThreshold(saveFigure=saveFigure, params=params)
    
    def plotPrecisionRecallVsThreshold(self, saveFigure=False, params={}):
        title = 'Decision Threshold'
        plt.figure(figsize=(8, 6))
        plt.plot(self.thresholds, self.precisions[:-1], 'b--', label='Precision')
        plt.plot(self.thresholds, self.recalls[:-1], 'g-', label='Recall')
        plt.xlabel('Threshold')
        plt.ylabel('Score')
        plt.title(title)
        plt.legend()
        plt.grid(True)
        
        if saveFigure:
            fileName = os.path.join(params['outputDir'], f"{params[DATASET_TYPE]}_{params[WINDOWSIZE]}_{params[STEP_SIZE]}_{title.replace(' ', '_')}.png")
            plt.savefig(fileName)
        plt.show()
        
    def getMetrics(self):
        return self.metrics, self.ROCCurve, self.PRCurve
    

    def getThreshold(self):
        return self.estimatedThreshold
