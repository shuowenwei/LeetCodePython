# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/top-k-frequent-elements/

"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countDic = {} 
        for n in nums:
            if n in countDic:
                countDic[n]+=1
            else:
                countDic[n] = 0 
        lst = [] 
        for key,value in countDic.items():
            lst.append((value,key))
        
        # sort by the first element in descending order     
        lst.sort(reverse=True)
        res = [] 
        for i in range(k):
            res.append(lst[i][1])
        return res
        """
        from collections import Counter
        numsCnter = Counter(nums)
        res = [(num, cnt) for num, cnt in numsCnter.items() ]
        res.sort(key=lambda x: x[1], reverse =True)
        return [x[0] for x in res[:k]]
        #rt = [] 
        #for i in range(k):
        #    rt.append(res[i][0]) 
        #return rt 
        """