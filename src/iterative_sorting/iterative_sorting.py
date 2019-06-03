# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        cur_index = i
        cur_value = arr[i]
        prev_index = i - 1
        while cur_value < arr[prev_index] and prev_index >= 0:
            arr[cur_index] = arr[prev_index]
            arr[prev_index] = cur_value
            prev_index -= 1
            cur_index -= 1
    return arr


print(selection_sort([2, 4, 3, 1]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
