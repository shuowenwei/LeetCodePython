# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/path-with-maximum-probability/

labuladong: https://labuladong.gitee.io/algo/1/10/

LC743, LC1514, LC1631

"""
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        import collections
        import heapq
        graph = collections.defaultdict(list)
        for (u,v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        hp = [(-1, start)] # probability are negative 
        heapq.heapify(hp)
        probToAllNodes = [0]*n # contains the result to return 
        while hp:
            print('start.......',probToAllNodes)
            curProb, curNode = heapq.heappop(hp)
            print(f'curProb={curProb}, curNode={curNode}')
            if curNode == end:
                return probToAllNodes[curNode]
            if -curProb >= probToAllNodes[curNode]:
                probToAllNodes[curNode] = -curProb
                for nextId, nextProb in graph[curNode]:
                    print(f'\t\tnextProb={nextProb}, nextId={nextId}')
                    if probToAllNodes[curNode] * nextProb > probToAllNodes[nextId]:
                        probToAllNodes[nextId] = probToAllNodes[curNode] * nextProb
                        heapq.heappush(hp, (-probToAllNodes[nextId], nextId))
            print('end.......',probToAllNodes)
            print('--------------------------------')
        print('final......',probToAllNodes)
        return 0.0 

# n = 3
# edges=[[0,1],[1,2],[0,2]]
# succProb=[0.5,0.5,0.2]
# start=0
# end=2
# ob = Solution() 
# ob.maxProbability(n, edges, succProb, start, end)
