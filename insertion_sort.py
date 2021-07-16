def insertion_sort(array):
    n = len(array)
    
    for i in range(1, n):
        value = array[i]
        hole = i

        while(hole>0 and array[hole-1]>value):
              array[hole] = array[hole-1]
              hole -= 1

        array[hole] = value

array = [4, 6, 2, 8, 1, 0, 9, 3, 5, 7]
insertion_sort(array)
print("Sorted array: ", array)

# Time complexity: O(n^2) worst case and average case


