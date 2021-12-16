# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/graph-valid-tree/

https://labuladong.gitee.io/algo/2/19/39/

LC323, LC130, LC990
LC547
LC261, LC1135, LC1584

"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range(n)]
        rank = [1]*n
        uf_count = n
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
        
        for u,v in edges:
            if isConnected(u, v):
                return False
            union(u, v)
            uf_count -= 1 
        return uf_count == 1 