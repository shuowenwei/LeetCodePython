# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/making-a-large-island/

LC323, LC130, LC990, LC547, LC847
"""
class UnionFind(object):
    def __init__(self, n):
        # n trees, not connected yet 
        self.cnt = n
        self.parent = [i for i in range(n)]
        self.size =  [1 for i in range(n)]
        
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]] # O(1)
            x = self.parent[x]
        return x
    
    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP == parentQ:
            return 
        if self.size[parentP] > self.size[parentQ]:
            self.parent[parentQ] = parentP
            self.size[parentP] += self.size[parentQ]
        elif self.size[parentP] <= self.size[parentQ]:
            self.parent[parentP] = parentQ
            self.size[parentQ] += self.size[parentP]
        self.cnt -= 1
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def getSize(self, n):
        return self.size[self.find(n)]

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        uf = UnionFind(col * row)
        visited = set()
        def getOneNeighbors(i, j):
            neighbors = []
            if i > 0 and grid[i-1][j] == 1:
                neighbors.append((i-1, j))
            if j > 0 and grid[i][j-1] == 1:
                neighbors.append((i, j-1))
            if i < row - 1 and grid[i+1][j] == 1:
                neighbors.append((i+1, j))
            if j < col - 1 and grid[i][j+1] == 1:
                neighbors.append((i, j+1))
            return neighbors 
        
        def dfs(i, j):
            if (i,j) in visited or grid[i][j] != 1:
                return 
            visited.add((i,j))
            cur_node = i*col + j
            for ni, nj in getOneNeighbors(i, j):
                nei_node = ni * col + nj
                uf.union(cur_node, nei_node)
                dfs(ni, nj)
                    
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i, j)

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    node = i*col + j
                    res = max(res, uf.getSize(node))
                elif grid[i][j] == 0:
                    tmp = 1
                    parents = set()
                    for ni, nj in getOneNeighbors(i, j):
                        nei_node = ni * col + nj 
                        parents.add(uf.find(nei_node))
                    for p_node in parents:
                        tmp += uf.getSize(p_node)
                    res = max(res, tmp)
        return res


        # solution 2: DFS only with hashmap
        if len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        visited = set()
        def getOneNeighbors(i, j):
            neighbors = []
            if i > 0 and grid[i-1][j] == 1:
                neighbors.append((i-1, j))
            if j > 0 and grid[i][j-1] == 1:
                neighbors.append((i, j-1))
            if i < row - 1 and grid[i+1][j] == 1:
                neighbors.append((i+1, j))
            if j < col - 1 and grid[i][j+1] == 1:
                neighbors.append((i, j+1))
            return neighbors 
        
        dct_island = collections.defaultdict(list)
        dct_grid2island = {}
        islandNumber = 0
        def dfs(i, j, islandNumber):
            if (i,j) in visited or grid[i][j] != 1:
                return 
            dct_island[islandNumber].append((i,j))
            dct_grid2island[(i,j)] = islandNumber
            visited.add((i,j))
            for ni, nj in getOneNeighbors(i, j):
                dfs(ni, nj, islandNumber)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i, j, islandNumber)
                    islandNumber += 1
                    
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res = max(res, len(dct_island[ dct_grid2island[(i,j)] ]))
                elif grid[i][j] == 0:
                    tmp = 1 # turn grid[i][j] to land 
                    parents = set() # find distint surrounding islands 
                    for ni, nj in getOneNeighbors(i, j):
                        parents.add(dct_grid2island[(ni,nj)])
                    for islandNumber in parents:
                        tmp += len(dct_island[islandNumber])
                    res = max(res, tmp)
        return res
