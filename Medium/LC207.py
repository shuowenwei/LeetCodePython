# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/course-schedule/

https://labuladong.gitee.io/algo/2/19/34/

https://labuladong.gitee.io/algo/2/19/35/

LC797, LC207, LC210

"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        import collections
        graph = collections.defaultdict(list)
        for s, t in prerequisites:
            graph[s].append(t)
        
        hasCycle = [False]
        visited = [False] * numCourses
        onPath = [False] * numCourses
        def traverse(graph, s):
            if onPath[s]:
                hasCycle.append(True)
                return
            if visited[s] or hasCycle[-1]:
                return
            visited[s] = True
            onPath[s] = True
            for neighbor in graph[s]:                
                traverse(graph, neighbor)
            onPath[s] = False

        for i in range(numCourses):
            traverse(graph, i)
            if hasCycle[-1]:
                break
        return not hasCycle[-1]