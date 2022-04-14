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
        # def getNeighbors(i, j):
        #     neighbors = []
        #     if i > 0:
        #         neighbors.append((i-1, j))
        #     if j > 0:
        #         neighbors.append((i, j-1))
        #     if i < row-1:
        #         neighbors.append((i+1, j))
        #     if j < col-1:
        #         neighbors.append((i, j+1))
        #     return neighbors
        
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
            # for ni, nj in getNeighbors(i,j):
            for di, dj in direction:
                ni = i + di
                nj = j + dj
                if 0 <= ni <= row-1 and 0 <= nj <= col-1:
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
        return - 1 
    
        # solution 2: DFS with memo, this won't work, refer to this link below
        # https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/1642476/The-Reason-Why-DFS-%2B-Memorize-Solution-DOESN'T-Work
        row, col = len(grid), len(grid[0])
        if row == 1 and col == 1:
            return 0 
        if k > row - 1 + col - 1:
            return row + col - 2
        
        self.res = float('inf')
        dp_tabel = {}
        def dfs_search(cur_step, i, j, grid, k):
            # invalid position or has been visited 
            if i < 0 or j < 0 or i > row - 1 or j > col - 1 or grid[i][j] == 2:
                return
            if (i,j,k) in dp_tabel:
                if dp_tabel[(i,j,k)] > cur_step:
                    dp_tabel[(i,j,k)] = cur_step
                return
            # not enough k
            if k == 0 and grid[i][j] == 1:
                return
            # valid path
            if i == row - 1 and j == col - 1:
                self.res = min(self.res, cur_step)
                return
            c = grid[i][j]
            grid[i][j] = 2
            if c == 1:
                k -= 1
            dp_tabel[(i,j,k)] = cur_step
            # always try to go right or down first
            dfs_search(cur_step + 1, i + 1, j,     grid, k)
            dfs_search(cur_step + 1, i,     j + 1, grid, k)
            dfs_search(cur_step + 1, i - 1, j,     grid, k)
            dfs_search(cur_step + 1, i,     j - 1, grid, k)
            grid[i][j] = c
            
        dfs_search(0, 0, 0, grid, k)
        return self.res if self.res != float('inf') else -1
