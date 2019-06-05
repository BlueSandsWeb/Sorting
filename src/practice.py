# RECURSION
# Space complexity? O(b-a)


def loop(n, stop):
    if(n > stop):
        return
    print(n)
    loop(n+1, stop)


# loop(0, 10)


# LOOPING O(1)
# Space complexity?
# for i in range(a, b):
#     print(i)

# Contrived recursive Big O fibbonaci sequence func


def foo(n):
    if n <= 0:
        return
    print(n)
    foo(n-1)
    foo(n-2)

# foo(1) #1
# foo(2) #2
# foo(3) #4
# foo(4) #7
# foo(5) #12
# foo(6) #20

# Quick Sort

# each partitioning pass takes O(n)


def partition(l):
    left = []
    pivot = l[0]
    right = []

    for v in l[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right

# O(n log(n))


def quicksort(l):
    if len(l) <= 1:
        return l

    left, pivot, right = partition(l)

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([5, 9, 3, 7, 2, 8, 1, 6, 4]))
