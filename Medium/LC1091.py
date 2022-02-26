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
        row, col = len(grid), len(grid[0])
        if grid[0][0] != 0:
            return -1 
        q = collections.deque()
        q.append((0 ,0))
        visited = set()
        d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        step = 0
        while q:
            size = len(q)
            step += 1
            for k in range(size):
                i, j = q.popleft()
                if i == row - 1 and j == col - 1:
                    return step 
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0<=ni<=row-1 and 0<=nj<=col-1 and (ni,nj) not in visited and grid[ni][nj] == 0:
                        q.append( (ni,nj) )
                        visited.add( (ni,nj) )
            # print(q)
        return -1
    
