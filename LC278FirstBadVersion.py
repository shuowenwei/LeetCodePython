# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/first-bad-version/

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1 
        end = n 
        while begin + 1 < end: 
            pivot = (begin+end)/2 
            if isBadVersion(pivot):
                end = pivot
            else:
                begin = pivot
        if isBadVersion(begin):
            return begin 
        return end 