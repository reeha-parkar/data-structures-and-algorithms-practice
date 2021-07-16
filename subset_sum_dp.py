def isSubsetSum(set, n, sum):
 
    # Base Cases
    if (sum == 0):
        return True
    if (n == 0):
        return False 
    # check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])
 
 
# Driver code
set = [3, 34, 5, 12, 4, 2]
sum = 9
n = len(set)
if (isSubsetSum(set, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
