#!/usr/bin/python3
"""
This module contains the function find_peak(list_of_integers).
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    A peak is an element that is greater than or equal to its neighbors.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak element if found, None otherwise.
    """

    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
