# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-path-sum/

https://labuladong.gitee.io/algo/3/25/84/

LC931, LC64, LC174, LC514
LC787
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])    
        dp_table = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    dp_table[i][j] = grid[i][j]
                elif i == 0:
                    dp_table[i][j] = grid[i][j] + dp_table[i][j-1]
                elif j == 0: 
                    dp_table[i][j] = grid[i][j] + dp_table[i-1][j]
                else:
                    dp_table[i][j] = grid[i][j] + min(dp_table[i][j-1], dp_table[i-1][j])
        return dp_table[row-1][col-1]

        # solution 2: top down 
        row, col = len(grid), len(grid[0])
        dp_table = {}
        dp_table[(0,0)] = grid[0][0]
        def dfs(i, j):
            if (i,j) in dp_table:
                return dp_table[(i,j)]
            res = 2 ** 32
            for di,dj in [(-1,0), (0,-1)]:
                if 0 <= i + di <= row - 1 and 0 <= j + dj <= col - 1:
                    res = min(res, grid[i][j] + dfs(i+di, j+dj) )
            dp_table[(i,j)] = res 
            return res 
        return dfs(row-1, col-1)