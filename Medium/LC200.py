# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-islands/

solution: https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution

https://labuladong.github.io/algo/4/29/108/

LC200, LC1254, LC1020, LC695, LC1905, LC694
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # solution 1: DFS with flooding the grid
        """
        if len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        def dfs(grid, i, j):
            if i < 0 or i > row-1 or j < 0 or j > col - 1 or grid[i][j] != '1':
                return 
            grid[i][j] = '#' # flood it
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
              
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res
        """
        # solution 2: without change grid 
        m, n = len(grid), len(grid[0])
        res = 0 
        visited = set()
        
        def dfs(grid, i, j):
            # already a visited island 
            if (i, j) in visited:
                return 
            m, n = len(grid), len(grid[0])
            # out of grid
            if i < 0 or j < 0 or i >= m or j >= n:
                return 
            # print(m,n,i,j)
            # meets the water
            if grid[i][j] == '0':
                return 
            # if on island, keep exploring around
            visited.add((i,j))
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res