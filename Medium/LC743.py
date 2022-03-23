# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/network-delay-time/

https://labuladong.gitee.io/algo/2/20/45/

LC743, LC1514, LC1631
"""
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        import collections
        import heapq
        graph = collections.defaultdict(list)
        for src, dst, weight in times:
            graph[src].append((dst, weight))
            
        hp = [(0, k)]
        heapq.heapify(hp)
        elapsedTime = [0] + [2**31-1]*n
        while hp:
            time, src_node = heapq.heappop(hp)
            if time < elapsedTime[src_node]:
                elapsedTime[src_node] = time
                for dst, weight in graph[src_node]:
                    heapq.heappush(hp, (time + weight, dst))
                    
        return max(elapsedTime) if max(elapsedTime) < 2**31-1 else -1
