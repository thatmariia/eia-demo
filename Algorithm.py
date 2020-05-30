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
        Algorithm("blah1", "blah blah 1"),
        Algorithm("blah2", "blah blah 2"),
        Algorithm("blah3", "blah blah 3")
    ]

    algorithms_row_2 = [
        Algorithm("blah4", "blah blah 4"),
        Algorithm("blah5", "blah blah 5"),
        Algorithm("blah6", "blah blah 6")
    ]

    return [algorithms_row_1, algorithms_row_2]
