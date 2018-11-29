# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-islands/

solution: https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution

"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0 
        res = 0
        def searchIsland(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return 
            grid[i][j] = '#'
            searchIsland(grid, i+1, j)
            searchIsland(grid, i-1, j)
            searchIsland(grid, i, j+1)
            searchIsland(grid, i, j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    searchIsland(grid, i, j)
                    res += 1
        return res 

        """
        if not grid:
            return 0 
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.searchIsland(grid, i, j)
                    res += 1
        return res 
    
    def searchIsland(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '#'
        self.searchIsland(grid, i+1, j)
        self.searchIsland(grid, i-1, j)
        self.searchIsland(grid, i, j+1)
        self.searchIsland(grid, i, j-1)
        """