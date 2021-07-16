A = [64, 25, 12, 22, 11]
 
# Traverse through all array elements except the last, it will be sorted anyway
for i in range(len(A)-1):
    # Find the minimum element in remaining unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
             
    # Swap the found minimum element with the first element       
    A[i], A[min_idx] = A[min_idx], A[i]
 
print("Sorted array is: ", A)

# Time complexity = O(n^2) Since two for loops
# Space complexity = O(1)
# in-place algorithm
