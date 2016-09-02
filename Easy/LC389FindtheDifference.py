# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/contest/2/problems/find-the-difference/

"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list_t = list(t)
        for e in s:
            list_t.remove(e)
        return list_t[0]
