from AlgorithmsManager import list_AvailableAlgorithms

def select_algorithm():
    """
    Asks a user on what algorithms they wanna train
    # TODO:: this is the part where we need input from website
    :return: selected by user algorithms
    """
    print("Available algorithms:")
    [print (i, end=", ") for i in list_AvailableAlgorithms()]
    print ()
    print ("Input the algorithm name")
    algorithm_name = input()
    # TODO:: check input
    return algorithm_name