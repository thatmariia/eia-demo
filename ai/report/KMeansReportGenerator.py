import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from KMeansAgent import KMeansAgent
from sklearn.mixture import GaussianMixture

colors = ["#E49273", "#404E7C", "#70877F", "#C4A77D", "#D1BCE3"]


class KMeansReportGenerator:

    def __init__(self, data, raw_data, filtered_indices,
                 kmeans_agent: KMeansAgent, col_names):
        self.data = data
        self.raw_data = raw_data
        self.filtered_indices = filtered_indices
        self.col_names = col_names

        self.predicted = kmeans_agent.predicted
        self.kmeans = kmeans_agent.kmeans
        self.k = kmeans_agent.k

        self.df = None
        self.recovered_df = raw_data

    def generate(self):
        self.combine_data_df()
        self.plot()
        self.reconstruct_raw_data()


        # TODO:: reconstruct db


    def combine_data_df(self):
        df_data = [np.append(i, j) for i, j in zip(self.data, self.predicted)]
        df_cols = self.col_names + ["Cluster"]

        self.df = pd.DataFrame(data=df_data, columns=df_cols)

    def reconstruct_raw_data(self):
        self.recovered_df["Cluster"] = np.nan

        i = 0
        for index in self.filtered_indices:
            self.recovered_df.loc[index, "Cluster"] = self.predicted[i]
            i += 1

    def make_ellipses(self, ax):
        gmm = GaussianMixture(n_components=self.k,
                              covariance_type="full",
                              max_iter=500, random_state=0)
        gmm.means_init = self.kmeans.cluster_centers_
        gmm.fit (self.data)

        for n in range(self.k):
            color = colors[n]
            if gmm.covariance_type == 'full':
                covariances = gmm.covariances_[n][:2, :2]
            elif gmm.covariance_type == 'tied':
                covariances = gmm.covariances_[:2, :2]
            elif gmm.covariance_type == 'diag':
                covariances = np.diag (gmm.covariances_[n][:2])
            elif gmm.covariance_type == 'spherical':
                covariances = np.eye (gmm.means_.shape[1]) * gmm.covariances_[n]
            v, w = np.linalg.eigh(covariances)
            u = w[0] / np.linalg.norm (w[0])
            angle = np.arctan2 (u[1], u[0])
            angle = 180 * angle / np.pi  # convert to degrees
            v = 2. * np.sqrt (2.) * np.sqrt (v)
            ell = mpl.patches.Ellipse(gmm.means_[n, :2], v[0], v[1],
                                      180 + angle, color=color)
            ell.set_clip_box(ax.bbox)
            ell.set_alpha(0.5)
            ax.add_artist(ell)
            ax.set_aspect('equal', 'datalim')



    def plot(self):
        if len(self.data[0]) > 2:
            # TODO:: maybe also plot for 3d
            return

        fig, ax = plt.subplots (figsize=(10, 10))

        for cluster in range(self.k):

            ax.scatter(
                    x=self.df[self.df["Cluster"] == cluster].iloc[:, 0],
                    y=self.df[self.df["Cluster"] == cluster].iloc[:, 1],
                    c=colors[cluster], marker="x",
                    label="Cluster "+str(cluster)
            )

        ax.scatter (
                x=self.kmeans.cluster_centers_[:, 0],
                y=self.kmeans.cluster_centers_[:, 1],
                s=250, marker='*',
                c='red', edgecolor='black',
                label='centroids'
        )

        self.make_ellipses(ax)

        plt.legend (scatterpoints=1)
        plt.xlabel(self.col_names[0])
        plt.ylabel(self.col_names[1])
        plt.grid ()
        plt.show ()




