from KMeansPreprocessor import KMeansPreprocessor
import pandas as pd


class DataPreprocessor:
    """
    Preprocesses raw test_datasets based what algorithm user wants to train it on
    """

    def __init__(self, algorithm, raw_data):
        self.algorithm = algorithm
        self.raw_data = raw_data

    def preprocess(self):

        return getattr (self, "_preprocess_" + self.algorithm.name)()
        #try:
        #    return getattr(self, "_preprocess_" + self.algorithm.name)()
        #except:
        #    print("No preprocessing for this algorithm")
        # TODO:: catch errors

    def _preprocess_kmeans(self):
        kmeans_preprocessor = KMeansPreprocessor(raw_data=self.raw_data)
        kmeans_preprocessor.preprocess()
        preprocessed_df = kmeans_preprocessor.retrieve_preprocessed_data()
        unindexed_list = preprocessed_df.values.T.tolist()[1:] # getting rid of index col
        return list(map(list, zip(*unindexed_list)))