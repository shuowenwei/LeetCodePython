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
        parent2size = {}
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
            if (i,j) in visited:
                return 
            visited.add((i,j))
            cur = i*col + j
            if grid[i][j] == 1:
                for ni, nj in getOneNeighbors(i, j):
                    uf.union(cur, ni*col + nj)
                    dfs(ni, nj)
                    
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i, j)
                    node = i * col + j
                    parent2size[uf.find(node)] = uf.getSize(node)
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
