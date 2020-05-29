import tensorflow as tf
import os
import random
import numpy as np

class KMeansAgent:
    # TODO:: FIX!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # NOTE:: started throwing some weird error Im too sleepy to figure out

    def __init__(self, data, k, nr_epochs):
        """
        :param data: preprocessed test_datasets
        :param k: number of clusters
        :param nr_epochs: duration of training
        """

        self.data = data
        self.k = k

        self.nr_dims = len(data[0])  # nr cols
        self.nr_features = len(data) # nr rows

        print("* self.nr_dims = ", self.nr_dims)
        print("* self.nr_features = ", self.nr_features)

        self.nr_epochs = nr_epochs

    def cluster(self):
        kmeans = tf.compat.v1.estimator.experimental.KMeans(num_clusters=self.k)

        #prev_centers = None
        cluster_centers = None

        for epoch in range(self.nr_epochs):
            # TODO:: epoch progress bar
            print("**** input fn type =", type(self._input_fn))
            print ("**** input fn =", self._input_fn)
            kmeans.train(self._input_fn)
            cluster_centers = kmeans.cluster_centers()
            #prev_centers = cluster_centers

        print("kmeans score =", kmeans.score(self._input_fn))
        print("cluster centers =", cluster_centers)

        cluster_indices = list(kmeans.predict_cluster_index(self._input_fn))
        for i, feature in enumerate (self.data):
            cluster_index = cluster_indices[i]
            center = cluster_centers[cluster_index]
            #print('feature:', feature, 'is in cluster', cluster_index, 'centered at', center)
            # TODO:: collect it all together

    def _input_fn(self):
        return tf.compat.v1.train.limit_epochs (
                tf.convert_to_tensor (self.data, dtype=tf.float32), num_epochs=1)
