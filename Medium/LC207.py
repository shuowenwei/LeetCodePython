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
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(set)
        for thenCanTake, takeFirst in prerequisites:
            graph[takeFirst].add(thenCanTake)
            indegree[thenCanTake] += 1
        
        count = 0 
        # res = []
        starters = [i for i in range(numCourses) if indegree[i] == 0]
        q = collections.deque(starters)
        while q:
            cur_node = q.popleft()
            # res.append(cur_node)
            count += 1 
            for nei_node in graph[cur_node]:
                indegree[nei_node] -= 1 
                if indegree[nei_node] == 0:
                    q.append(nei_node)
        # print(res, count)
        if count != numCourses:
            # // 存在环，拓扑排序不存在
            return False
        return True