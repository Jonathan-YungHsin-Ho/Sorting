# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    index_A = 0
    index_B = 0
    while i < elements:
        if index_A == 4:
            merged_arr[i] = arrB[index_B]
            index_B += 1
        elif index_B == 4:
            merged_arr[i] = arrA[index_A]
            index_A += 1
        elif arrA[index_A] < arrB[index_B]:
            merged_arr[i] = arrA[index_A]
            index_A += 1
        elif arrB[index_B] < arrA[index_A]:
            merged_arr[i] = arrB[index_B]
            index_B += 1
        i += 1
    return merged_arr


print('END', merge([9, 10, 11, 12], [1, 2, 4, 8]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
