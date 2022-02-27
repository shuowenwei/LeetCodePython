# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/evaluate-division/

"""
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dctGraph = collections.defaultdict(list)
        for sd, value in zip(equations, values):
            dctGraph[sd[0]].append((sd[1], value))
            dctGraph[sd[1]].append((sd[0], 1/value))
        
        def bfs(s, t):
            if s not in dctGraph or t not in dctGraph:
                return -1.0
            for x, value in dctGraph[s]:
                if x == t:
                    return value
            q = collections.deque()
            visited = set()
            q.append( (s, 1.0) )
            visited.add(s)
            while q:
                size = len(q)
                for _ in range(size):
                    cur, cur_value = q.popleft()
                    if cur == t:
                        dctGraph[s].append((t, cur_value))
                        return cur_value
                    for neighbor, value in dctGraph[cur]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append( (neighbor, cur_value * value) )
            return -1.0
        return [bfs(s,t) for s,t in queries]