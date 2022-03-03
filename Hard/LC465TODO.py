# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/optimal-account-balancing/

"""
import collections
class Solution(object):
    def minTransfers(self, tranctions):
        dictBanks = collections.defaultdict(list)
        for p1, p2, amount in tranctions:
            dictBanks[p1].append(amount)
            dictBanks[p2].append(-amount)
        # print(dictBanks)
        dictBanks = {people : sum(lstAmount) for people, lstAmount in dictBanks.items() if sum(lstAmount) != 0 }
        lstAmount = [v for _, v in dictBanks.items()]
        # lstAmount = [-700, -92, 379, 160, -585, 383, -532, 680, -509, 529, 161, 670, -544]
        self.res = 2 ** 32 
        def backtracking(lstAmount, index, conuter):
            n = len(lstAmount)
            while index < n and lstAmount[index] == 0:
                index += 1
            if index == n:
                self.res = min(self.res, conuter)
            for i in range(index, n):
                if (lstAmount[i] < 0 and lstAmount[index] > 0) or  (lstAmount[i] > 0 and lstAmount[index] < 0):
                    lstAmount[i] += lstAmount[index]
                    backtracking(lstAmount, index + 1, conuter + 1)
                    lstAmount[i] -= lstAmount[index]
        backtracking(lstAmount, 0, 0)
        print('result from backtracking... ',self.res)
        return self.res


import random 
peoplle = 'ABCDEFGHIGKLMN'
tranctions = []
for _ in range(1000):
    p1 = random.choice(peoplle)
    p2 = random.choice(peoplle)
    amount = int(random.uniform(1, 100))
    tranctions.append([p1, p2, amount])

ob = Solution()
print(ob.minTransfers(tranctions))


    

