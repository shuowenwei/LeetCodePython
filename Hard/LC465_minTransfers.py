import collections
from heapq import heapify, heappop, heappush
from random import random
res = [0]
# tranctions = [['A', 'B', 200], ['B', 'C', 200], ['C', 'A', 100]]
def sortenList(lstAmount):
    if len(lstAmount) == 0:
        return
    # dictAmoun = {la:0 for la in lstAmount}
    # key2remove = []
    # for k, _ in dictAmoun.items():
    #     if -k in dictAmoun:
    #         key2remove.append(k)
    #         key2remove.append(-k)
    # for key in set(key2remove):
    #     del dictAmoun[key]
    # res[0] += len(set(key2remove)) // 2

    # lstAmount = list(dictAmoun.keys())
    lstAmount.sort(key = lambda x: -abs(x))
    if len(lstAmount) == 0:
        return
    else:
        print(lstAmount)
        first = lstAmount.pop(0)
        second = lstAmount.pop(0)
        lstAmount.append(first + second)
        res[0] += 1
        sortenList(lstAmount)

def minMoneyExchange(tranctions):
    dictBanks = collections.defaultdict(list)
    for p1, p2, amount in tranctions:
        dictBanks[p1].append(amount)
        dictBanks[p2].append(-amount)
    # print(dictBanks)
    dictBanks = {people : sum(lstAmount) for people, lstAmount in dictBanks.items() if sum(lstAmount) != 0 }
    print(dictBanks)
    lstAmount = [v for _, v in dictBanks.items()]
    print('lstAmount', lstAmount, sum(lstAmount))
    # lstAmount = [30, -22, 10, -15, 5, -8] #[-196, -159, -158, -155, -105, -85, -64, 21, 28, 80, 146, 316, 331] # 
    # positiveCounter = 0
    # negativeCounter = 0
    # for amount in lstAmount:
    #     if amount > 0: 
    #         positiveCounter += 1
    #     else:
    #         negativeCounter += 1
    # sortenList(lstAmount)
    # print(res[0], max(positiveCounter, negativeCounter))
    # return res[0], max(positiveCounter, negativeCounter)
    counter = 0 
    positive_heap = [-a for a in lstAmount if a > 0]
    negative_heap = [a for a in lstAmount if a < 0]
    heapify(positive_heap)
    heapify(negative_heap)
    while positive_heap and negative_heap:
        pos = - heappop(positive_heap)
        neg = heappop(negative_heap)
        res = pos + neg
        counter += 1
        if res > 0:
            heappush(positive_heap, -res)
        if res < 0:
            heappush(negative_heap, res)
    return counter 

# tranctions = [['A', 'B', 200], ['B', 'C', 200], ['C', 'A', 100]]
# tranctions = [['A', 'B', 200], ['B', 'C', 200], ['C', 'A', 100]]
# print(minMoneyExchange(tranctions))

import random 
peoplle = 'ABCDEFGHIGKLMN'
tranctions = []
for _ in range(1000):
    p1 = random.choice(peoplle)
    p2 = random.choice(peoplle)
    amount = int(random.uniform(1, 100))
    tranctions.append([p1, p2, amount])
print(minMoneyExchange(tranctions))
