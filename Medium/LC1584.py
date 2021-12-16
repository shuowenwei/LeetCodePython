# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/min-cost-to-connect-all-points/

https://labuladong.gitee.io/algo/2/19/39/
https://mp.weixin.qq.com/s/dJ9gqR3RVoeGnATlpMG39w

LC323, LC130, LC990
LC547
LC261, LC1135, LC1584

"""
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        weights = set()
        numPoints = len(points)
        if numPoints == 1:
            return 0
        for i in range(numPoints): 
            for j in range(i+1, numPoints):
                x, y = points[i]
                m, n = points[j]
                weights.add( (i, j, abs(m-x)+abs(n-y)) )
                
        parent = [i for i in range(numPoints)]
        rank = [1]*(numPoints)
        uf_count = numPoints
        minSpanningTree = 0 
        
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
        
        def isConnected(n1, n2):
            return find(n1) == find(n2)
        
        sorted_weights = sorted(list(weights), key=lambda x: x[2])
        for u,v,w in sorted_weights:
            if isConnected(u, v):
                continue
            union(u, v)
            minSpanningTree += w
            uf_count -= 1 
            if uf_count == 1:
                return minSpanningTree 
        
        
        

