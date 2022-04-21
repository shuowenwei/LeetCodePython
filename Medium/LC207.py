# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/course-schedule/

https://labuladong.gitee.io/algo/2/20/37/

LC797, LC207, LC210, LC630, LC2115
LC785, LC886
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
        for thenTake, takefirst in prerequisites: 
            graph[takefirst].append(thenTake)
            inDegree[thenTake] += 1 
        
        starters = [course for course in range(numCourses) if inDegree[course] == 0] 
        q = collections.deque(starters)
        numCourseCanBeTaken = 0 
        # res = []
        while q:
            cur_course = q.popleft()
            numCourseCanBeTaken += 1
            # res.append(cur_course)
            for nei_course in graph[cur_course]:
                inDegree[nei_course] -= 1 
                if inDegree[nei_course] == 0:
                    q.append(nei_course)
        return numCourseCanBeTaken == numCourses
        # # print(res, numCourseCanBeTaken)
        # if numCourseCanBeTaken != numCourses: # // 存在环，拓扑排序不存在
        #     return False
        # return True