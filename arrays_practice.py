import array

#printing array
def print_array(line, arr):
    print(line, end=" ")
    for i in range (0, len(arr)):
        print (arr[i], end=" ")
        
#i ~ signed integers
arr = array.array('i', [1, 2, 3])
print_array("The new created array is: ", arr)
 
print("\r")
 
#append(): inserts new value at end
arr.append(4);
print_array("The appended array is: ", arr)
     
#arr.insert(index, value)
arr.insert(2, 5)
print("\r")
print_array("The array after insertion is: ", arr)

print("\r")

#reverses the array 
arr.reverse()
print_array("The array after reversing is: ", arr)

print("\r")

#arr.pop(p): removes the value at pth position
arr.pop(1)
print_array("The array after popping element at index 1 is: ", arr)

print("\r")

#arr.remove(k): removes the first occurrence of k; gives an Exception if not available
arr.remove(5)
print_array("The array after removing element 3 is: ", arr)

print("\r")

#index(k): returns the index of first occurrence of k
print("The index of {} is {}".format(4, arr.index(4)))





