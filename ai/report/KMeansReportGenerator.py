import matplotlib.pyplot as plt
import pandas as pd
from KMeansAgent import KMeansAgent

class KMeansReportGenerator:

    def __init__(self, data, kmeans_agent: KMeansAgent, maps, col_names):
        self.data = data
        self.maps = maps
        self.col_names = col_names

        self.predicted = kmeans_agent.predicted
        self.kmeans = kmeans_agent.kmeans
        self.k = kmeans_agent.k

    def generate(self):
        df = self.combine_data()
        print(df)
        # TODO:: make a graph

        # TODO:: reconstruct db


    def combine_data(self):
        df_data = [self.data[i] + [self.predicted[i]] for i in range(len(self.data))]
        df_cols = self.col_names + ["Cluster"]

        return pd.DataFrame(data=df_data, columns=df_cols)




    def plot(self):
        fig, ax = plt.subplots (figsize=(10, 10))



