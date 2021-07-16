# sets the largest element at its place in each pass


def bubble_sort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

                
def modified_bubble_sort(arr):
    n = len(arr)
    flag = 0
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
        if flag == 0: return


 
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
 
modified_bubble_sort(arr)
 
print ("Sorted array is:")
print(arr)

# Time complexity - O(n^2) Since two for loops
# Space complexity - O(1) Since
