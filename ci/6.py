"""
Find the closest pair from two sorted arrays.
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.
"""


def findClosestPair(arr1, arr2, x):
    if len(arr1) == 0 or len(arr2) == 0:
        return None
    i = 0
    j = len(arr2) - 1
    min_diff = abs(arr1[0] + arr2[j] - x)
    closest_pair = (arr1[0], arr2[j])
    while i < len(arr1) and j >= 0:
        if abs(arr1[i] + arr2[j] - x) < min_diff:
            min_diff = abs(arr1[i] + arr2[j] - x)
            closest_pair = (arr1[i], arr2[j])
        if arr1[i] + arr2[j] < x:
            i += 1
        else:
            j -= 1
    return closest_pair


print(findClosestPair([1, 4, 5, 7], [10, 20, 30, 40], 42))
