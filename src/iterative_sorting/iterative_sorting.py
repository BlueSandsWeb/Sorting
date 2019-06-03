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


# print(selection_sort([2, 4, 3, 1]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True and len(arr) > 1:
        num_swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp1 = arr[i]
                temp2 = arr[i+1]
                arr[i] = temp2
                arr[i+1] = temp1
                num_swaps += 1
        if num_swaps == 0:
            return arr
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr


# print(bubble_sort([2, 5, 4, 1, 3]))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
