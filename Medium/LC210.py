# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/course-schedule-ii/

https://labuladong.gitee.io/algo/2/20/37/

LC797, LC207, LC210, LC630, LC2115
LC785, LC886
topology sort: LC207, LC210, LC2050
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
        for thenCanTake, takeFirst in prerequisites:
            graph[takeFirst].append(thenCanTake)
        
        self.hasCycle = False
        visited = set() #[False] * numCourses
        onPath = [False] * numCourses
        postorder = []
        def traverse(graph, s):
            if onPath[s]:
                self.hasCycle = True
            if s in visited or self.hasCycle:
                return
            # // 前序遍历位置
            visited.add(s)
            onPath[s] = True
            for neighbor in graph[s]:                
                traverse(graph, neighbor)
             # // 后序遍历位置
            postorder.append(s)
            onPath[s] = False
        
        for i in range(numCourses):
            traverse(graph, i)
            if self.hasCycle:
                return []
        # print(postorder[::-1])
        return postorder[::-1]

        # Soltion 2: BFS with TopologySort 
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
        return res if len(res) == numCourses else []
        # if len(res) != numCourses: # // 存在环，拓扑排序不存在
    
numCourses = 2
prerequisites = [[1,0]]

ob= Solution()
ob.findOrder(numCourses, prerequisites)