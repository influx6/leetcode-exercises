# Python program to partition the array
# using Hoare's Partition Algorithm
#
# Hoare's Partition Algorithm is generally faster than Lomuto's because it performs fewer swaps and makes only one traversal of the array, leading to better time complexity in practice.
# It works in-place and does not require extra space, unlike the naive partitioning method which uses a temporary array.
# It can be used to implement a stable version of Quick Sort with the right adjustments, though it is not inherently stable.
# We can easily modify the algorithm to consider the first element (or any other element) as pivot by swapping first and last elements and then using the same code.


# Function to partition the array according to pivot index element
def partition(arr):
    n = len(arr)
    pivot = arr[0]

    i = -1
    j = n
    while True:

        # find next element larger than pivot from the left
        while True:
            i += 1
            if arr[i] >= pivot:
                break

        # find next element smaller than pivot from the right
        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        # if left and right crosses each other no swapping required
        if i > j:
            break

        # swap larger and smaller elements
        arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2, 7, 1, 10]
    partition(arr)

    for num in arr:
        print(num, end=' ')
