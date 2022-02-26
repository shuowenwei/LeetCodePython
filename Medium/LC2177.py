# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

"""
class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 != 0:
            return []
        else:
            mid = num / 3
            return [mid - 1, mid, mid + 1]
