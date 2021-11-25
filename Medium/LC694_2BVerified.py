# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-distinct-islands/

"""
class Solution(object):
    def countSubIslands(self, grid):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs_floodfill(grid, i, j, seq, s):
            m, n = len(grid), len(grid[0])
            # out of grid or already meets the water
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            # preorder 
            grid[i][j] = 0 # 1 is land, flood this land by setting to 0
            seq.append(s)
            dfs_floodfill(grid, i-1, j, seq, 1) 
            dfs_floodfill(grid, i+1, j, seq, 2) 
            dfs_floodfill(grid, i, j-1, seq, 3) 
            dfs_floodfill(grid, i, j+1, seq, 4)
            # postorder 
            seq.append(-s)

        # similiar to LC1254 from now on 
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    seq = []
                    dfs_floodfill(grid, i, j, seq, '999')
                    res.add(','.join([str(s) for s in seq]))
        return len(s)
