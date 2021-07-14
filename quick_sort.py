def partition(start, end, array):
     
    partition_index = start
    pivot = array[end]
     
    for i in range(start, end):
        if array[i]<=pivot:
            array[i], array[partition_index] = array[partition_index], array[i]
            partition_index += 1
            
    array[end], array[partition_index] = array[partition_index], array[end]
    return partition_index
     
# The main function that implements QuickSort
def quick_sort(start, end, array):
     
    if (start < end):
         
        # p is partitioning index, array[p] is at right place
        p = partition(start, end, array)
         
        # Sort elements before partition
        # and after partition
        quick_sort(start, p-1, array)
        quick_sort(p+1, end, array)
         
# Driver code
array = [1, -1, 13, 4, 1, 0]
quick_sort(0, len(array)-1, array)
 
print(f'Sorted array: {array}')


# Time complexity = O(nlogn) Average Case (for randomized quick sort)
# Time complexity = O(n^2) Worst case (can almost always be avoided)
# Space complexity = O(1) in-place
