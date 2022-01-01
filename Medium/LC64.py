# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-path-sum/

https://labuladong.gitee.io/algo/3/26/84/

LC931, LC64, LC174
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])    
        dp_table = [[0 for i in range(col)] for j in range(row)]
        dp_table[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0:
                    dp_table[i][j] = grid[i][j] + dp_table[i][j-1]
                elif j == 0: 
                    dp_table[i][j] = grid[i][j] + dp_table[i-1][j]
                else:
                    dp_table[i][j] = grid[i][j] + min(dp_table[i][j-1], dp_table[i-1][j])
        
        return dp_table[row-1][col-1]
