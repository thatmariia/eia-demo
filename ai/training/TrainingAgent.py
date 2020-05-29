from KMeansAgent import KMeansAgent
from training_functions import *

class TrainingAgent:

    def __init__(self, algorithm, data, nr_epochs=100):
        self.algorithm = algorithm
        self.data = data
        self.nr_epochs = nr_epochs


    def train(self):
        print("TrainingAgent: self.algorithm.name = ", "_train_" + self.algorithm.name)

        getattr (self, "_train_" + self.algorithm.name) ()  # TODO:: catch errors

    def _train_kmeans(self):
        k = select_k()
        kmeans_agent = KMeansAgent(data=self.data, k=k, nr_epochs=self.nr_epochs)
        kmeans_agent.cluster()
        #return "training..."