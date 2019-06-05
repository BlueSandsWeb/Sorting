# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    for i in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA.pop(0)
            else:
                merged_arr[i] = arrB.pop(0)
        elif len(arrA) > 0:
            merged_arr[i] = arrA.pop(0)
        elif len(arrB) > 0:
            merged_arr[i] = arrB.pop(0)

    # print(merged_arr)
    return merged_arr


# merge([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        pivot = round(len(arr)/2)
        left = merge_sort(arr[:pivot])
        print("left: ", left)
        right = merge_sort(arr[pivot:])
        print("right: ", right)

        new_arr = merge(left, right)
        print("new_arr: ", new_arr)
        return new_arr


# print("Merge sort end: ", merge_sort([2, 5, 7, 3, 1, 4, 6]))

# STRETCH: implement an in-place merge sort algorithm


test_array = [1, 2, 3, 4]
test_array[0], test_array[1] = test_array[1], test_array[0]
print(test_array)


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
