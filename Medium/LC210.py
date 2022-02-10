# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/course-schedule-ii/

https://labuladong.gitee.io/algo/2/19/35/

LC797, LC207, LC210, LC630
LC785, LC886
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        import collections
        graph = collections.defaultdict(list)
        for s, t in prerequisites:
            graph[s].append(t)
        
        hasCycle = [False]
        visited = [False] * numCourses
        onPath = [False] * numCourses
        postorder = []
        def traverse(graph, s):
            if onPath[s]:
                hasCycle[0] = True
            if visited[s] or hasCycle[0]:
                return
            # // 前序遍历位置
            visited[s] = True
            onPath[s] = True
            for neighbor in graph[s]:                
                traverse(graph, neighbor)
             # // 后序遍历位置
            postorder.append(s)
            onPath[s] = False
        
        for i in range(numCourses):
            traverse(graph, i)
            if hasCycle[0]:
                return []
        return postorder  # wrong: res = postorder[::-1]

numCourses = 2
prerequisites = [[1,0]]

ob= Solution()
ob.findOrder(numCourses, prerequisites)