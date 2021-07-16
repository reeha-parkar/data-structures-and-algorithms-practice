# Time complexity: O(n^2)
def get_pairs(array, number):
    for i in range(len(array)):
        for j in range(i+1, len(array)-1):
            if array[i]+array[j] == number:
                print((array[i], array[j]))


# Time_complexity: O(n)
# space complexity: O(n)
def get_pairs_with_set(array, number):
    s = set()
    for i in range(len(array)):
        temp = number-array[i]
        if temp in s:
            print((array[i], temp))
        s.add(array[i])


# can also sort and then 


array = [1, 4, 4, 5, 63, 6, 3, 5, 4, 4]
number = 8

get_pairs_with_set(array, number)
