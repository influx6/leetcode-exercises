# Python program to partition the array
# using Lomuto Partition Algorithm
def partition(arr):
    n = len(arr)
    pivot = arr[n - 1]

    # i acts as boundary between smaller and
    # larger element compared to pivot
    i = -1
    for j in range(n):

        # If smaller element is found expand the
        # boundary and swapping it with boundary element.
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place the pivot at its correct position
    arr[i + 1], arr[n - 1] = arr[n - 1], arr[i + 1]

if __name__ == "__main__":
    arr = [5, 13, 6, 9, 12, 11, 8]
    partition(arr)
    for ele in arr:
    	print(ele, end = ' ')
