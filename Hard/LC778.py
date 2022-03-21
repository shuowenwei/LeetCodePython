# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/swim-in-rising-water/

LC407, LC778
"""
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        hp = []
        heappush(hp, (grid[0][0], 0, 0))
        visited = set()
        row, col = len(grid), len(grid[0])
        res = 0
        while hp:
            t, i, j = heappop(hp)
            if (i,j) == (row-1, col-1):
                return t
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni = i + di
                nj = j + dj
                if 0<=ni<row and 0<=nj<col and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    tmp = max(t, grid[ni][nj]) 
                    heappush(hp, (tmp, ni, nj))
