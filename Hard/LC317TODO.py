# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/shortest-distance-from-all-buildings/

https://blog.csdn.net/qq_37821701/article/details/108906696

"""
import collections
class Solution:
    def shortestDistance(self, grid):
        def helper(i,j):
            visited = set()
            buildings = set()
            q = collections.deque()
            q.append((i,j,0))
            visited.add((i,j))
            total_step = 0
            dirs = [[0,1],[0,-1],[-1,0],[1,0]]
            
            while q:
                i, j, step = q.popleft()
                if grid[i][j] == 1 and (i, j) not in buildings:
                    total_step += step
                    buildings.add((i, j))
                if len(buildings) == num_buildings:
                    break
                if grid[i][j] != 1:
                    for d in dirs:
                        x = i + d[0]
                        y = j + d[1]
                        if 0<=x<m and 0<=y<n and (x,y) not in visited and grid[x][y] != 2:
                            q.append((x, y, step + 1))
                            visited.add((x, y))
            return total_step if len(buildings )== num_buildings else -1
        
        m,n = len(grid),len(grid[0])
        num_buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_buildings += 1
        
        min_step = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    total_step = helper(i, j)
                    if total_step != -1 and total_step < min_step:
                        min_step = total_step

        return min_step if min_step != float('inf') else -1




class Solution:
    def shortestDistance(self, grid):
        def bfs(i,j):
            visited = [[False]*n for _ in range(m)]
            q = collections.deque()
            q.append((i, j, 1))
            dirs = [[0,1], [0,-1], [-1,0], [1,0]]
            
            while q:
                i,j,dis = q.popleft()
                for d in dirs:
                    x = i + d[0]
                    y = j + d[1]
                    if 0<=x<m and 0<=y<n and not visited[x][y] and grid[x][y] == 0:
                        distance[x][y] += dis
                        reach_num[x][y] += 1
                        q.append((x, y, dis + 1))
                        visited[x][y] = True
                
        m, n = len(grid), len(grid[0])
        distance = [[0]*n for _ in range(m)]
        reach_num = [[0]*n for _ in range(m)]
        building_num = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i,j)
                    building_num += 1
        
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_num[i][j] == building_num:
                    min_dist = min(min_dist, distance[i][j])
        
        return min_dist if min_dist!=float('inf') else -1
