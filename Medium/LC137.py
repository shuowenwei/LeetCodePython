# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number-ii/submissions/

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

This is a silly solution that uses much more extra memory 

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution with extra space
        # dict_count = {}
        # for n in nums:
        #     if n in dict_count:
        #         dict_count[n] += 1
        #     else:
        #         dict_count[n] = 1
        # for k,v in dict_count.items():
        #     if v == 1:
        #         return k 
        # solution 2: without using extra memory
        return (3*sum(set(nums)) - sum(nums)) // 2


