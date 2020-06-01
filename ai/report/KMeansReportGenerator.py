import matplotlib.pyplot as plt
import pandas as pd
from KMeansAgent import KMeansAgent

class KMeansReportGenerator:

    def __init__(self, data, kmeans_agent: KMeansAgent, map, col_names):
        self.data = data
        self.map = map
        self.col_names = col_names

        self.predicted = kmeans_agent.predicted
        self.kmeans = kmeans_agent.kmeans
        self.k = kmeans_agent.k

        self.df = None

    def generate(self):
        self.combine_data_df()
        self.reverse_map_df()
        print(self.df)
        # TODO:: make a graph

        # TODO:: reconstruct db


    def combine_data_df(self):
        df_data = [self.data[i] + [self.predicted[i]] for i in range(len(self.data))]
        df_cols = self.col_names + ["Cluster"]

        self.df = pd.DataFrame(data=df_data, columns=df_cols)

    def reverse_map_df(self):
        inv_map = {}

        for col in self.df.columns:
            if col in self.map.keys():

                inv_map[col] = {v: k for k, v in self.map[col].items ()}
                print(inv_map[col])
                self.df[col] = self.df[col].map(inv_map[col])


    def plot(self):
        fig, ax = plt.subplots (figsize=(10, 10))



