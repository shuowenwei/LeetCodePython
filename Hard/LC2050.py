# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/parallel-courses-iii/

https://leetcode.com/problems/parallel-courses-iii/discuss/1537479/C%2B%2BPython-Topology-Sort-O(M%2B-N)-Clean-and-Concise

LC1834, LC2050, LC630
"""
class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        inDegree = [0] * n
        for s, d in relations:
            graph[s-1].append(d-1)
            inDegree[d-1] += 1
            
            
        distant = [0] * n
        q = deque()
        for node in range(n):
            if inDegree[node] == 0:
                distant[node] = time[node]
                q.append(node)

        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                distant[nxt] = max(distant[nxt], distant[cur] + time[nxt] )
                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    q.append(nxt)

        return max(distant)

