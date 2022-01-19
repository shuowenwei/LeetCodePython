# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/linked-list-cycle-ii/

https://labuladong.gitee.io/algo/4/32/131/

LC698, LC78, LC46, LC77, LC22, LC659
LC51, LC37
- backtrack
"""
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def backtrack(nums, start, path):
            if start == len(nums):
                if len(path) >= 3:
                    return True
                else:
                    return False
            # add to the end of existing sequence
            if len(path) > 0:
                if nums[start] - path[-1] == 1:
                    path.append(nums[start])
                if backtrack(nums, start+1, path):
                    return True
                path.pop()
                
            # start a new sequence
            path = [nums[start]]
            if backtrack(nums, start+1, path):
                return True
            path.pop()
            return False 
        
        return backtrack(nums, 0, [])
