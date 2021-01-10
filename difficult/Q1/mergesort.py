def merge(left, right):
    """ Function to merge sub-arrays together an also sort them """

    sorted_list = []
    # Break out of loop if any one of the array gets empty
    while len(left) and len(right):
        # Pick the smaller among the smallest element of left and right sub arrays
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    """ Concatenating the leftover elements (in case we didn't go through the entire left or right array) """
    return [*sorted_list, *left, *right]


def merge_sort(List):
    """ Function to sort {List} using merge sort algorithm """

    # Base case or terminating case
    if len(List) < 2:
        return List
    mid = len(List) // 2
    left = List[:mid]
    right = List[mid:]
    return merge([*merge_sort(left)], [*merge_sort(right)])


print(merge_sort([9, 7, 6, 5, 1, 4, 8, 3, 2])  == ([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # True
print(
    merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
    == ([17, 20, 26, 31, 44, 54, 55, 77, 93])
)  # True
print(merge_sort([]) == [])  # True
