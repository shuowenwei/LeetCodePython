# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/excel-sheet-column-number/

"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0 
        for i in range( len(s) ): 
            n +=  ( ord(s[i]) - 64 ) * pow(26,len(s)-i-1)
            
        return n 