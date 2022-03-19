# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/optimal-account-balancing/

LC698, LC465
Google Onsite Coding Question
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
        print(lstAmount)
        self.res = 2 ** 32 
        def backtracking(lstAmount, start, conuter):
            n = len(lstAmount)
            while start < n and lstAmount[start] == 0:
                start += 1
            if start == n:
                self.res = min(self.res, conuter)
            for i in range(start, n):
                if (lstAmount[i] < 0 and lstAmount[start] > 0) or (lstAmount[i] > 0 and lstAmount[start] < 0):
                    lstAmount[i] += lstAmount[start]
                    backtracking(lstAmount, start + 1, conuter + 1)
                    lstAmount[i] -= lstAmount[start]
        backtracking(lstAmount, 0, 0)
        print('result from backtracking... ',self.res)
        return self.res

    # solution 2: 
    def minTransfers_LC698(self, tranctions):
        dictBanks = collections.defaultdict(list)
        for p1, p2, amount in tranctions:
            dictBanks[p1].append(amount)
            dictBanks[p2].append(-amount)
        # print(dictBanks)
        dictBanks = {people : sum(lstAmount) for people, lstAmount in dictBanks.items() if sum(lstAmount) != 0 }
        lstAmount = [v for _, v in dictBanks.items()]
        # lstAmount = [-700, -92, 379, 160, -585, 383, -532, 680, -509, 529, 161, 670, -544]
        
        print(lstAmount)
        max_buckets = len(lstAmount)
        used_nums = [False] * len(lstAmount)
        lstAmount.sort(key=lambda x: -abs(x))
        def backtrack(nums, index, each_sum, subset):
            if index == len(nums):
                if len(set(subset)) == 1 and subset[0] == each_sum:
                    return True 
                else:
                    return False
            for i in range(min_k):
                if subset[i] + nums[index] > each_sum:
                    continue # pruning here
                subset[i] += nums[index]
                if backtrack(nums, index+1, each_sum, subset):
                    return True
                subset[i] -= nums[index]
        
        for min_k in range(2, max_buckets):
            print('result from minTransfers_LC698 ... ', min_k)
            subset = [0] * min_k
            if backtrack(lstAmount, 0, 0, subset):
                return min_k 
        return min_k
    
    
import random 
peoplle = 'ABCDEFGHIGKLMN'
tranctions = []
for _ in range(500):
    p1 = random.choice(peoplle)
    p2 = random.choice(peoplle)
    amount = int(random.uniform(1, 100))
    tranctions.append([p1, p2, amount])

ob = Solution()
print(ob.minTransfers(tranctions))
print(ob.minTransfers_LC698(tranctions))


    

