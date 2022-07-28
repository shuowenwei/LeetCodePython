# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/course-schedule/

https://labuladong.gitee.io/algo/2/20/37/

LC797, LC207, LC210, LC630, LC2115
LC785, LC886
topology sort: LC207, LC210, LC2050
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
        
        self.hasCycle = False
        visited = set()
        
        onPath = [False] * numCourses
        def traverse(graph, s):
            if onPath[s]:
                self.hasCycle = True
                return
            if s in visited or self.hasCycle:
                return
            visited.add(s)
            onPath[s] = True
            for neighbor in graph[s]:                
                traverse(graph, neighbor)
            onPath[s] = False

        for i in range(numCourses):
            traverse(graph, i)
            if self.hasCycle:
                break
        return not self.hasCycle

        # BFS, refer to LC210
        import collections 
        graph = collections.defaultdict(list)
        inDegree = collections.defaultdict(int)
        
        for nextCourse, prevCourse in prerequisites:
            graph[prevCourse].append(nextCourse)
            inDegree[nextCourse] += 1
            
        startCourses = [c for c in range(numCourses) if inDegree[c] == 0]
        q = collections.deque(startCourses)
        res = []
        while q:
            cur_course = q.popleft()
            res.append(cur_course)
            for next_course in graph[cur_course]:
                inDegree[next_course] -= 1 
                if inDegree[next_course] == 0:
                    q.append(next_course)
        # print(res)
        return len(res) == numCourses
        # if len(res) != numCourses: # // 存在环，拓扑排序不存在