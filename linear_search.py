arr = [1, 2, 3, 4, 5]
search = 2
n = len(arr)
found = 0

# linear search = traverse all elements of the array and check each of them
# Complexity = O(n)
for i in range(n):
    if arr[i] == search:
        print("{0} is found at index {1}".format(search, i))
        found = 1
        break
if not found:
    print("Not found")
