# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/parallel-courses-iii/

https://leetcode.com/problems/parallel-courses-iii/discuss/1537479/C%2B%2BPython-Topology-Sort-O(M%2B-N)-Clean-and-Concise

LC1834, LC2050, LC630
topology sort
"""
class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        import collections
        graph = collections.defaultdict(list)
        inDegree = [0] * n
        for prevCourse, nextCourse in relations:
            # course index shift by 1
            graph[prevCourse-1].append(nextCourse-1)
            inDegree[nextCourse-1] += 1
            
        startCourses = [c for c in range(n) if inDegree[c] == 0]
        minMonths = time[::] #same: [time[c] if inDegree[c] == 0 else 0 for c in range(n)]
        q = collections.deque(startCourses)

        while q: 
            curCourse = q.popleft()
            for nextCourse in graph[curCourse]:
                minMonths[nextCourse] = max(minMonths[nextCourse], minMonths[curCourse] + time[nextCourse])
                inDegree[nextCourse] -= 1 
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
                    
        return max(minMonths)

