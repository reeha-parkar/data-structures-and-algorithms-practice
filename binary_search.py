def b_search(arr, low, high, find):
    if low<=high:
        mid = low + (high-low)//2
        # Not doing mid = (high+low)//2 so that the addition won't surpass
        # the max possible int value and memory error does not occur
        if arr[mid]==find:
            return mid
        elif arr[mid]<find:
            return b_search(arr, mid+1, high, find)
        else:
            return b_search(arr, low, mid-1, find)
    else:
        return -1




arr = [1, 2, 3, 4, 5, 6, 7, 8]
find = 1
index = b_search(arr, 0, len(arr)-1, find)

if index==-1:
    print("The element wasn't found")

else:
    print("{0} was found at index {1}".format(find, index))
