def sum_of_squares(f_list):
    total_sum = 0
    for i in range(len(f_list)):
        total_sum += f_list[i]*f_list[i]
    return total_sum

def get_combination_sum(k, numbers, target, partial=[]):
    s = sum(partial)
    if s == target and len(partial) == k:
        current_sum = sum_of_squares(partial)
        #print(current_sum)
        sum_list.append(current_sum)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        get_combination_sum(k, numbers, target, partial+[n])

t = int(input()) # test cases
for i in range(t):
    nk = input()
    n = int(nk.split(' ')[0]) # no.of bowls
    k = int(nk.split(' ')[1]) # no.of children
    c_per_bowl = input()
    c = [] # list of original chocolates per bowl in all bowls
    #print(c_per_bowl.split(' '))
    for i in range(n):
        c.append(int(c_per_bowl.split(' ')[i]))
    #print (n, k, c)


    final_list = []
    if sum(c) == k:
        for i in range(k):
            final_list.append(1)
        #print(final_list)
        minimum_sum = sum_of_squares(final_list)
        print(minimum_sum)
    else:
        numbers = [i for i in range(1,sum(c)+1)]
        #print(numbers)
        sum_list = []
        get_combination_sum(k, numbers, numbers[-1])
        print(min(sum_list))
        
            
    

