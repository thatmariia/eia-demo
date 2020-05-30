class Algorithm:
    """
    Just for the overview of algorithms
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description


def get_algorithms() -> [Algorithm]:
    # TODO:: put actual legit algorithms here
    algorithms_row_1 = [
        Algorithm("linear regression", "linear approach to modeling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables)."),
        Algorithm("K-means", "Partitions observations into k clusters in which each observation belongs to the cluster with the nearest mean."),
        Algorithm("CNN", "Performs images recognition, images classifications.")
    ]

    algorithms_row_2 = [
        Algorithm("Desicion trees", "Creates a model that predicts the value of a target variable by learning simple decision rules inferred from the data features."),
        Algorithm("PCA", "Reduces the dimensionality of data, increases interpretability while minimizing information loss."),
        Algorithm("Perceptron", "Decides whether or not an input, represented by a vector of numbers, belongs to some specific class")
    ]

    return [algorithms_row_1, algorithms_row_2]
