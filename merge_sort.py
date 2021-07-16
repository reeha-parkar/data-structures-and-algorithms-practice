# Time complexity - O(nlogn) (worst case)
# Space complexity - O(n) /or/ theta(nlogn)
# divide and conquer algorithm
# recursive algorithm
# stable sorting algorithm (preserves the relative order of records with same key)
# Not an in-place sorting algorithm (extra space is taken)

def merge(left, right, array):
    l = len(left)
    r = len(right)
    i = j = k = 0

    # comparing both the left and right arrays
    while i<l and j<r:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
            
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # if there are any leftovers in either left or right (only one while will run)
    while i<l:
        array[k] = left[i]
        i += 1
        k += 1
    while j<r:
        array[k] = right[j]
        j += 1
        k += 1

def merge_sort(array):
    n = len(array)
    if n<2: return
    mid = n//2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, array)
    return array

sort_this_array = [3, 6, 8, 1, 9, 2, 7, 5, 4, 0]
sorted_array = merge_sort(sort_this_array)
print("sorted array: ", sorted_array)
        

            
