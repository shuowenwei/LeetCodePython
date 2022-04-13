# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

refer to https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/451787/Python-O(m*n*k)-BFS-Solution-with-Explanation
- BFS
"""
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        from collections import deque
        row, col = len(grid), len(grid[0])
        if row == 1 and col == 1:
            return 0 
        if k > row - 1 + col - 1:
            return row + col - 2
        def getNeighbors(i, j):
            neighbors = []
            if i > 0:
                neighbors.append((i-1, j))
            if j > 0:
                neighbors.append((i, j-1))
            if i < row-1:
                neighbors.append((i+1, j))
            if j < col-1:
                neighbors.append((i, j+1))
            return neighbors
        
        q = deque()
        visited = set()
        dp_tabel = {}
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        q.append((0,0,k))
        visited.add((0,0,k))
        dp_tabel[(0,0,k)] = 0
        while q:
            i,j,k = q.popleft()
            if i == row - 1 and j == col - 1: # target = (row-1, col-1)
                return dp_tabel[(i,j,k)]
            for ni, nj in getNeighbors(i,j):
                if grid[ni][nj] == 1 and k > 0:
                    if (ni,nj,k-1) not in visited:
                        dp_tabel[(ni,nj,k-1)] = dp_tabel[(i,j,k)] + 1
                        q.append((ni,nj,k-1))
                        visited.add((ni,nj,k-1))
                if grid[ni][nj] == 0:
                    if (ni,nj,k) not in visited:
                        dp_tabel[(ni,nj,k)] = dp_tabel[(i,j,k)] + 1
                        q.append((ni,nj,k))
                        visited.add((ni,nj,k))
        return -1 