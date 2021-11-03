# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/height-checker/

"""

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0 
        for h, sh in zip(heights, sorted(heights)):
            if h != sh:
                res += 1
        return res