# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/random-pick-index/

https://labuladong.gitee.io/algo/4/30/119/

LC382, LC398
"""
class Solution(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dict = {}
        for index, n in enumerate(nums):
            if n not in self.dict: 
                self.dict[n] = [index]
            else:
                self.dict[n].append(index)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random 
        return random.choice(self.dict[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)