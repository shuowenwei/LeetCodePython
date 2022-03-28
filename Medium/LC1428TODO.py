# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

refer to https://snowan.gitbook.io/study-notes/leetcode/30daychallenge/leftmost-column-with-at-least-a-one

"""
class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        # solution 1: binary search
        # Time Complexity: O(MlogN)
        # Space Complexity: O(1)
        if len(binaryMatrix) == 0:
            return -1 
        res = 2 ** 32 
        row, col = len(binaryMatrix), len(binaryMatrix[0])
        for r in range(row):
            res = min(res, binarySearch(binaryMatrix, r, col))
        return res if res !=  2 ** 32  else -1 
        
        def binarySearch(binaryMatrix, row, col): 
            if binaryMatrix[row][col-1] == 0:
                return 2 ** 32
            if binaryMatrix[row][0] == 1:
                return 0
            left, right = 0, col - 1
            while left <= right:
                mid = left + (right - left) // 2
                if binaryMatrix[row][mid] == 1:
                    right = mid - 1 
                else:
                    left = mid + 1
            return left 
        
        
        # solution 2: Linear Time, search from top-right
        # Time Complexity: O(M+N)
        # Space Complexity: O(1)
        if len(binaryMatrix) == 0:
            return -1 
        res = 2 ** 32 
        row, col = len(binaryMatrix), len(binaryMatrix[0])
        res = -1
        r = 0
        c = col - 1 
        while r < row and c >= 0:
            if binaryMatrix[r][c] == 1:
                res = c 
                c -= 1
            else:
                r += 1
        return res 