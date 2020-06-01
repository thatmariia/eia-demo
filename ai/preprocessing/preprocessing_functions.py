import numpy as np
import pandas as pd

def select_columns(raw_data):
    """
    Asks a user which columns should be trained
    # TODO:: this is the part where we need input from website
    # TODO:: before asking a user, explain what columns should be
    :param raw_data: the exact test_datasets user uploaded
    :return: selected by user columns
    """
    column_names = raw_data.columns
    print("Available columns:")
    [print (i, end=", ") for i in column_names]
    print ()
    print ("Input column names for KMeans separated by ', '")
    column_names = input().split (", ")
    # TODO:: check input
    return column_names

def generate_map_column(data, column: str):
    """
    Maps every category in column to a number
    NOTE:: should make sure dataset isnt longer than the number of ints
    :return: dict[object-category : int]
    """

    uniques_categories = list(set([str(el) for el in data[column].tolist()]))
    map = {}

    for i in range(len(uniques_categories)):
        map.update({ str(uniques_categories[i]) : i })

    return map

def map_data_to_float(data):
    """
    Turns the whole dataframe into floats
    :return: df filled with floats and map from generate_map_column
    """
    map = {}
    for col in data.columns:

        if np.issubdtype (data[col].dtype, np.number):
            data[col] = data[col]
        else:
            data[col] = data[col].astype(str)
            map[col] = generate_map_column (data=data, column=col)
            data[col] = data[col].map(map[col])#data.replace({col: map[col]})

        data[col] = data[col].astype (float)

    return data
