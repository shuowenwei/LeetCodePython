# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/shortest-path-in-binary-matrix/

"""
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return - 1
        row, col = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return -1 
        q = collections.deque()
        q.append((0, 0, 1))
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1),
                      (1,1), (1,-1), (-1,1), (-1,-1)]
        while q:
            size = len(q)
            i, j, step = q.popleft()
            if (i,j) == (row - 1, col - 1):
                return step 
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0<=ni<=row-1 and 0<=nj<=col-1 and (ni,nj) not in visited and grid[ni][nj] == 0:
                    q.append((ni, nj, step + 1))
                    visited.add((ni, nj))
        return -1
    
