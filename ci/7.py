"""
Given a sorted array and a number x, find the pair in array whose sum is closest to x

"""


def find_closest(arr, x):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        if x - arr[0] < arr[1] - x:
            return arr[0]
        else:
            return arr[1]
    mid = len(arr) // 2
    if x - arr[mid] < arr[mid + 1] - x:
        return arr[mid]
    else:
        return arr[mid + 1]


print(find_closest([1, 4, 5, 7, 8], 7))
