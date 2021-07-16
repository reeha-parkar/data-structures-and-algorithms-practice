# Python program to sort an array with 0,1 and 2 in a single pass 

# Function to sort array 
def DNFS(arr): 
  low = 0
  high = len(arr)- 1
  mid = 0
  while mid <= high: 
    if arr[mid] == 0: 
      arr[low],arr[mid] = arr[mid],arr[low] 
      low = low + 1
      mid = mid + 1
    elif arr[mid] == 1: 
      mid = mid + 1
    else: 
      arr[mid],arr[high] = arr[high],arr[mid] 
      high = high - 1
  return arr 
	
# Function to print array 
def printArray(arr): 
    for k in arr: 
        print(k, end=' ')
    print()
	

# Driver Program 
arr = [0, 0, 1, 1, 2, 0, 1, 2] 
arr_size = len(arr)

print("Array before DNFS algorithm")
printArray(arr) 

arr = DNFS(arr) 

print("Array after DNFS algorithm")
printArray(arr) 
