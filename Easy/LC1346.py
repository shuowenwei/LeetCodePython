# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/check-if-n-and-its-double-exist/


"""

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashTable = {}
        for a in arr:
            if a*2 in hashTable:
                return True
            if a%2 == 0 and a/2 in hashTable:
                return True
            if a not in hashTable:
                hashTable[a] = 0
        return False 