from enum import Enum
from algorithms_functions import *


class AlgorithmsManager():
    """
    Asks user for an algorithm, and for extra parameters if applicable
    """

    def select(self):
        algorithm = self._get_algorithm(select_algorithm().lower())
        return algorithm


    def _get_algorithm(self, algorithm_name):
        try:
            return AvailableAlgorithms[algorithm_name]
        except ValueError:
            print("This algorithm is not supported")



class AvailableAlgorithms(Enum):
    kmeans = 0

def list_AvailableAlgorithms():
    return [f.name for f in AvailableAlgorithms]