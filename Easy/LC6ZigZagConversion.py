# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/zigzag-conversion/

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ['']*numRows

        rowNum = 0
        incre = 1
        for e in s: 
            res[rowNum] += e
            if rowNum == 0:
                incre = 1
            if rowNum == numRows-1:
                incre = -1
            rowNum = rowNum + incre
            
        resString = '' 
        for eachList in res:
            resString += eachList
        return resString