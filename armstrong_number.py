n = input()

numbers = list(map(int, list(n)))

n = int(n)
print(numbers)
sum = 0
for i in numbers:
    sum += i**(len(numbers))
print(sum)
if sum==n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
