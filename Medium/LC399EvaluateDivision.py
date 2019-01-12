# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/evaluate-division/

solution: https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        graph = {}
        def buildGradh(equations, values): 
            def addEdge(f, t, value):
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
                    
            for vertices, value in zip(equations, values):
                f, t = vertices
                addEdge(f, t, value)
                addEdge(t, f, 1/value)
                
        def findPath(query):
            b, e = query
            if b not in graph or e not in graph:
                return -1.0 
            
            q = collections.deque([(b, 1.0)])
            visited = set()
            
            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product 
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
            return -1.0
        buildGradh(equations, values)
        return [findPath(e) for e in queries]
    