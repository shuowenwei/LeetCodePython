# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/toeplitz-matrix/

https://leetcode.com/problems/toeplitz-matrix/discuss/113385/Python-Easy-and-Concise-Solution

"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        for i in range(1, row): 
            for j in range(1, col): 
                top_left_i = i - i
                top_left_j = j - i
                if top_left_j >= 0 and matrix[i][j] != matrix[top_left_i][top_left_j]:
                    return False
                elif top_left_j < 0:
                    top_left_i = i - j
                    top_left_j = j - j
                    if matrix[i][j] != matrix[top_left_i][top_left_j]:
                        return False
        return True 

        # concise! 
        m = matrix
        row, col = len(matrix), len(matrix[0])
        return all(m[i][j] == m[i+1][j+1] for i in range(row-1) for j in range(col-1))