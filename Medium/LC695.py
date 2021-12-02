# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/max-area-of-island/

labuladong: https://leetcode.com/problems/number-of-enclaves/

LC200, LC1254, LC1020, LC695, LC1905, LC694

"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])            
        def dfs_floodfill(grid, i, j):
            m, n = len(grid), len(grid[0])
            # out of grid or already meets the water
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0 # 1 is land, flood this land by setting to 0
            return dfs_floodfill(grid, i-1, j) \
                + dfs_floodfill(grid, i+1, j) \
                + dfs_floodfill(grid, i, j-1) \
                + dfs_floodfill(grid, i, j+1) + 1

            
        # similiar to LC1254 from now on 
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs_floodfill(grid, i, j)) 
        return res
