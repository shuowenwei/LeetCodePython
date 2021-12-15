# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

LC323, LC130, LC990
LC547

https://www.youtube.com/watch?v=8f1XPm4WOUc: 
"""
class Solution(object):
    def countComponents(self, n, edges):
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            res = n1 
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res 
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else: 
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges: 
            res -= union(n1, n2)
        return res
        """
        other solutions: DFS
        """