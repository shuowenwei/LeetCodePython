# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://labuladong.gitee.io/algo/3/23/69/

https://labuladong.gitee.io/algo/3/23/69/

LC931, LC64, LC174
"""
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def getMinLastLevel(dp_table, i, j):
            if i == 0:
                return 0
            res = [ dp_table[i-1][j] ]
            if j > 0: 
                res.append(dp_table[i-1][j-1])
            if j < len(dp_table[0])-1:
                res.append(dp_table[i-1][j+1])
            return min(res)
        
        row, col = len(matrix), len(matrix[0])    
        dp_table = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                dp_table[i][j] = matrix[i][j] + getMinLastLevel(dp_table, i, j)
        return min(dp_table[row-1][:])
        
        
