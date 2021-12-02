# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-sub-islands/

LC200, LC1254, LC1020, LC695, LC1905, LC694

"""
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])
        def dfs_floodfill(grid, i, j):
            m, n = len(grid), len(grid[0])
            # out of grid or already meets the water
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            grid[i][j] = 0 # 1 is land, flood this land by setting to 0
            dfs_floodfill(grid, i-1, j) 
            dfs_floodfill(grid, i+1, j) 
            dfs_floodfill(grid, i, j-1) 
            dfs_floodfill(grid, i, j+1)

        # similiar to LC1254 from now on 
        res = 0
        for i in range(m):
            for j in range(n):
                # not a sub-island, flood them all 
                if grid1[i][j] == 0 and grid2[i][j] == 1: 
                    dfs_floodfill(grid2, i, j)
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1: 
                    res += 1
                    dfs_floodfill(grid2, i, j)
        return res 