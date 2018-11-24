# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/zigzag-conversion/

"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -1
        dictS = {}
        for e in s:
            if e in dictS: 
                dictS[e] += 1
            else:
                dictS[e] = 1
        for i in range(len(s)):
            if dictS[s[i]] == 1:
                res = i 
                return res
        return res 