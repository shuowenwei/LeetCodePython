# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/search-a-2d-matrix/

"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        # target 
        while left <= right: 
            mid = left + (right - left) / 2
            i, j = mid / col, mid % col
            if matrix[i][j] < target: 
                left = mid + 1 
            elif matrix[i][j] > target: 
                right = mid - 1
            elif matrix[i][j] == target:
                return True
        return False 
        
