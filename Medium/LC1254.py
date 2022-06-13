# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-closed-islands/

labuladong: https://labuladong.gitee.io/algo/1/7/

LC200, LC1254, LC1020, LC695, LC1905, LC694

"""
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        def dfs_floodfill(grid, i, j):
            # out of grid or already meets the water
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 1:
                return 
            grid[i][j] = 1 # 0 is land, flood this land by setting to 1
            dfs_floodfill(grid, i-1, j)
            dfs_floodfill(grid, i+1, j)
            dfs_floodfill(grid, i, j-1)
            dfs_floodfill(grid, i, j+1)

        # Floodfill the land attached to the side 
        for i in range(row): 
            dfs_floodfill(grid, i, 0)
            dfs_floodfill(grid, i, col-1)
        for j in range(col):
            dfs_floodfill(grid, 0, j)
            dfs_floodfill(grid, row-1, j)
        # similiar to LC200 from now on 
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    res += 1
                    dfs_floodfill(grid, i, j)
        return res