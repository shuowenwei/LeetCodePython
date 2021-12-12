# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/network-delay-time/

labuladong: https://labuladong.gitee.io/algo/1/10/

LC743, LC1514, LC1631

"""
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        import collections
        import heapq
        def getAdjacent(i,j,m,n):
            adj = []
            if i > 0: 
                adj.append((i-1,j))
            if j > 0: 
                adj.append((i,j-1))
            if i < m-1: 
                adj.append((i+1,j))
            if j < n-1: 
                adj.append((i,j+1))
            return adj

        graph = collections.defaultdict(list)
        m, n = len(heights), len(heights[0])
        for i in range(m):
            for j in range(n):
                for adj_i, adj_j in getAdjacent(i,j,m,n):
                    graph[(i,j)].append((abs(heights[i][j] - heights[adj_i][adj_j]), (adj_i, adj_j)))
        hp = [(0, (0,0))]
        end = (m-1, n-1)
        heapq.heapify(hp)
        efferts = [[2**31-1 for j in range(n)] for i in range(m)]
        while hp:
            curEffort, curNode = heapq.heappop(hp)
            if curNode[0] == m-1 and curNode[1] == n-1:
                return curEffort
            if curEffort < efferts[curNode[0]][curNode[1]]:
                efferts[curNode[0]][curNode[1]] = curEffort
                for nextEfforts, nextNode in graph[(curNode[0], curNode[1])]:
                    adj_i, adj_j = nextNode
                    heapq.heappush(hp, (max(nextEfforts,curEffort), (adj_i, adj_j)))
                    # A route's effort is the maximum absolute difference in heights 
                    # between two consecutive cells of the route.
        return -1 


heights = [[1,2,2],[3,8,2],[5,3,5]]
ob = Solution()
ob.minimumEffortPath(heights)