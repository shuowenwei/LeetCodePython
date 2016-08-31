# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/permutations/

solution reference link: https://discuss.leetcode.com/topic/54786/another-very-intuitive-recursive-python-solution

"""

class Solution(object):
    def rem(self, nums, n):
        nums.remove(n)
        return nums

    def permute_(self, nums, perm, res):
        if not nums:
            res.append(perm)
        else:
            for n in nums:
                self.permute_(self.rem(nums[:], n), perm+[n], res)
        
    def permute(self, nums):
        res = []
        self.permute_(nums, [], res)
        return res