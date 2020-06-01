from preprocessing_functions import *

class KMeansPreprocessor():
    """
    Does KMeans-specific preprocessing
    """

    def __init__(self, raw_data: pd.DataFrame):
        self.map = {}
        self.preprocessed_data = raw_data
        self.column_names = None

    def preprocess(self):
        #TODO:: maybe think if some other things can be done, maybe scaling?

        # select column names
        self.column_names = select_columns(raw_data=self.preprocessed_data)
        self.preprocessed_data = self.preprocessed_data[self.column_names]

        # remove columns with nan
        self.preprocessed_data = self.preprocessed_data.dropna().reset_index()

        # check for categorical preprocessed_data
        self.preprocessed_data, self.map = map_data_to_float(data=self.preprocessed_data)

