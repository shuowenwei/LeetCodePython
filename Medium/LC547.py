# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-provinces/

LC323, LC130, LC990, LC547, LC847
LC261, LC1135, LC1584
"""
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = [False]*len(isConnected)
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor, isAdjacent in enumerate(isConnected[node]):
                if isAdjacent == 1 and not visited[neighbor]:
                    dfs(neighbor)

        res = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                res += 1
        return res

""" solution 2: union find
        parent = [i for i in range(len(isConnected))]
        rank = [1]*len(isConnected)
        
        def find(x): 
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        res = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(i):
                if isConnected[i][j] == 1:
                    res -= union(i,j)
        return res 
"""