def mergeArrays(list1, list2):
    list1.extend(list2)

    def quick_sort(unsorted_list):
        if len(unsorted_list) < 2:
            return unsorted_list
        pivot = unsorted_list.pop()  # Use the last element as the first pivot
        greater = []  # All elements greater than pivot
        lesser = []  # All elements less than or equal to pivot
        for element in unsorted_list:
            (greater if element > pivot else lesser).append(element)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

    return list(quick_sort(set(list1)))


a = [-1, 1, 3, 5, 7, 9]
b = [-2, 2, 3, 4, 5, 6]
print(mergeArrays(a, b))
