# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/check-if-n-and-its-double-exist/

LC1, LC1346
"""
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict_double = {}
        for a in arr:
            if a*2 in dict_double:
                return True
            if a%2==0 and a/2 in dict_double:
                return True
            dict_double[a] = 0
        return False