# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-provinces/

"""

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [False]*len(M)
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor, isAdjacent in enumerate(M[node]):
                if isAdjacent == 1 and not visited[neighbor]:
                    dfs(neighbor)

        res = 0
        for i in range(len(M)):
            if not visited[i]:
                dfs(i)
                res += 1
        return res
