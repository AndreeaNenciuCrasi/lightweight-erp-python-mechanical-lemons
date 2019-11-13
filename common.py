""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    # your code

    return generated


def is_larger(current_largest, new_item):
    if new_item > current_largest:
        return True
    else:
        return False


def remove_from_list(table, id_):
    new_table = []
    ID = 0
    for data in table:
        if id_[ID] not in data[ID]:
            new_table.append(data)
    return new_table
