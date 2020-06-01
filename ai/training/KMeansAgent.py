from sklearn.cluster import KMeans

class KMeansAgent:

    def __init__(self, data, k, nr_epochs=5000):
        """
        :param data: preprocessed test_datasets
        :param k: number of clusters
        :param nr_epochs: duration of training
        """

        self.data = data

        self.k = k

        self.nr_epochs = nr_epochs

    def cluster(self):
        kmeans = KMeans (
                n_clusters=self.k, init='random',
                n_init=10, max_iter=self.nr_epochs,
                tol=1e-04, random_state=0
        )
        predicted = kmeans.fit_predict(self.data)

        return predicted


