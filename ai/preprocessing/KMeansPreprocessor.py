from preprocessing_functions import *
from sklearn.preprocessing import MinMaxScaler

class KMeansPreprocessor():
    """
    Does KMeans-specific preprocessing
    """

    def __init__(self, raw_data: pd.DataFrame):
        self.map = {}
        self.preprocessed_data = raw_data
        self.column_names = None
        self.filtered_data = raw_data
        self.filtered_indices = None

    def preprocess(self):
        #TODO:: maybe think if some other things can be done, maybe scaling?

        # select column names
        self.column_names = select_columns(raw_data=self.filtered_data)
        self.filtered_data = self.filtered_data[self.column_names]

        # remove columns with nan
        self.filtered_data = self.filtered_data.dropna()

        # check for categorical preprocessed_data
        self.filtered_data = map_data_to_float(data=self.filtered_data)

        # saving indices we're gonna train on NOTE:: assume 1d index
        self.filtered_indices = list(self.filtered_data.index.values)


        # apply minmax scaling
        scaler = MinMaxScaler()
        self.preprocessed_data = scaler.fit_transform(self.filtered_data)


