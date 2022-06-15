
# reffer to https://stackoverflow.com/questions/18394733/generating-a-random-number-between-1-7-by-rand5
# Rejection sampling: https://en.wikipedia.org/wiki/Rejection_sampling

from random import randint
from collections import Counter

def rand5():
    return randint(0, 4)

def rand7():
    x = 5 * rand5() + rand5()
    if x < 21: # 7, 14 also works, but with more rejections
        return x % 7 + 1 
    
rand_nums = []
for i in range(1000000):
    get7 = rand7()
    if get7:
        rand_nums.append(get7)
    
freq = Counter(rand_nums)
for num, freqs in freq.items():
    print(num, freqs, freqs/len(rand_nums))