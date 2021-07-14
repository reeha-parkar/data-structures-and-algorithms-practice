from itertools import combinations

def get_count(lst):
    total_count = []
    for sub in lst:
        current_count = [i for i in range(len(S)) if S.startswith(sub, i)]
        total_count.append(len(current_count))
    return sum(total_count)
    
S = 'BANANA'
vowels = list('AEIOU')
res = [S[x:y] for x, y in combinations(range(len(S) + 1), r=2)]
cbn = list(set(res))
kevin = []
stuart = []
for i in cbn:
    if i[0] in vowels:
        kevin.append(i)
    else:
        stuart.append(i)
stuart = sorted(stuart)
kevin = sorted(kevin)

stuart_count = get_count(stuart)
kevin_count = get_count(kevin)
#print(stuart_count, kevin_count)

if stuart_count > kevin_count:
    print('Stuart {}'.format(stuart_count))

elif stuart_count < kevin_count:
    print('Kevin {}'.format(kevin_count))

else:
    print('Draw')

