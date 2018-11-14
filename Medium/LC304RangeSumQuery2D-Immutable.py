# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/range-sum-query-2d-immutable

solution reference link:  https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/75448/Sharing-My-Python-solution 
"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix is None or not matrix: 
            return 
        m, n = len(matrix), len(matrix[0]) 
        self.matrix_sums = [[0 for j in range(n+1)] for i in range(m+1)] 
        for i in range(1,m+1):
            for j in range(1,n+1):
                self.matrix_sums[i][j] = matrix[i-1][j-1] + self.matrix_sums[i-1][j] + self.matrix_sums[i][j-1] - self.matrix_sums[i-1][j-1]
            
    def sumRegion(self, row1, col1, row2, col2): 
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.matrix_sums[row2 + 1][col2 + 1] - self.matrix_sums[row1][col2+1] - self.matrix_sums[row2+1][col1] + self.matrix_sums[row1][col1]
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
