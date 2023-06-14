#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_scr = float('-inf')
    bestkey = None
    for key, value in a_dictionary.items():
        if value > max_scr:
            max_scr = value
            bestkey = key

    return bestkey
