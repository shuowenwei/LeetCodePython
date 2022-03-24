# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/pascals-triangle/

"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0: 
            return []
        if numRows == 1:
            return [[1]]
            
        triangle = [[1]] 
        for i in range(1, numRows):
            nextLevel=[1] 
            for j in range(1, i):
                nextLevel.append( triangle[i-1][j-1] + triangle[i-1][j])
            nextLevel.append(1)
            triangle.append(nextLevel)
        return triangle
