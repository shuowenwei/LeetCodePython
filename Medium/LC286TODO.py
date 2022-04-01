# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/walls-and-gates/

https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/286.html?q=

"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        rooms: List[List[int]]
        Do not return anything, modify rooms in-place instead.
        """
        # solution 1: DFS: https://zhenyu0519.github.io/2020/03/07/lc286/#sample-io
        if len(rooms) == 0:
            return []
        
        row, col = len(rooms), len(rooms[0])
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(x, y, dis):
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and rooms[nx][ny] > rooms[x][y]:
                    rooms[nx][ny] = dis + 1
                    dfs(nx, ny, dis + 1)

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    dfs(i, j, 0)
        # We iterate each cell will cost O(m*n) where m*n is the size of the 2D list. 
        # Each cell will also iterate four directions O(m*n*4). In total O(4*m*n)
        
    def wallsAndGates_BFS(self, rooms):
        # solutioin 2: BFS
        if len(rooms) == 0:
            return []
        
        row, col = len(rooms), len(rooms[0])
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        import collections
        q = collections.deque()
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            size = len(q)
            for _ in range(size):
                i, j, dis = q.popleft()
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < row and 0 <= nj < col and rooms[ni][nj] > dis + 1:
                        rooms[ni][nj] = dis + 1
                        q.append((ni, nj, dis + 1))
sol = Solution()
rooms=[[2**32, -1, 0, 2**32],
       [2**32, 2**32, 2**32, -1],
       [2**32, -1, 2**32, -1],
       [0, -1, 2**32, 2**32]]
sol.wallsAndGates(rooms)
print(rooms)

rooms=[[2**32, -1, 0, 2**32],
       [2**32, 2**32, 2**32, -1],
       [2**32, -1, 2**32, -1],
       [0, -1, 2**32, 2**32]]
sol.wallsAndGates_BFS(rooms)
print(rooms)