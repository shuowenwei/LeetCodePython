# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/combination-sum/


solution reference link: 

https://discuss.leetcode.com/topic/23142/python-dfs-solution

https://discuss.leetcode.com/topic/44038/combination-sum-i-ii-and-iii-java-solution-see-the-similarities-yourself

"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = [] 
        #candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res 
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return 
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
