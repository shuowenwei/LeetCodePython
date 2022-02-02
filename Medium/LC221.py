# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximal-square/

LC221, LC1277
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row, col = len(matrix), len(matrix[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    if r == 0 or c == 0:
                        res = max(res, 1)
                    else:
                        new_cell_val = min(int(matrix[r-1][c]),
                                           int(matrix[r][c-1]), 
                                           int(matrix[r-1][c-1])) + int(matrix[r][c])
                        res = max(res, new_cell_val)
                        matrix[r][c] = new_cell_val
        return res**2
        