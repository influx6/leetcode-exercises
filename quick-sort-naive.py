# Function to partition the array according
# to pivot index element. Uses the last element as pivot.
#
# - It is a stable partitioning algorithm, meaning it preserves the relative order of duplicate elements. We can make Quick Sort stable by using it
# - It is slower than other partitioning algorithms because it requires multiple traversals of the array and uses extra space for storing elements.
# - We can easily modify the algorithm to consider the first element (or any other element) as pivot by swapping first and last elements and then using the same code.
#
def partition(arr):
    n = len(arr)

    # Last element will be the pivot value
    pivot = arr[n - 1]

    # create a temp array to store
    # the elements in order
    temp = [0] * n
    idx = 0

    # First fill elements smaller than or equal to
    # pivot, into the temp array
    for i in range(n):
        if arr[i] <= pivot:
            temp[idx] = arr[i]
            idx += 1

    # Now fill the elements greater than pivot
    # into the temp array
    for i in range(n):
        if arr[i] > pivot:
            temp[idx] = arr[i]
            idx += 1

    # copy the elements from temp to arr
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [5, 13, 6, 9, 12, 11, 8]
    partition(arr)

    for ele in arr:
    	print(ele, end = ' ')
