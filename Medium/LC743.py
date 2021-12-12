# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/network-delay-time/

labuladong: https://labuladong.gitee.io/algo/1/10/

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
        graph = {}
        for src, dst, weight in times:
            if src in graph:
                graph[src].append((dst, weight))
            else:
                graph[src] = [(dst, weight)]

        import heapq
        hp = [(0, k)]
        heapq.heapify(hp)
        elapsedTime = [0] + [2**31-1]*n
        while hp:
            time, node = heapq.heappop(hp)
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                if graph.get(node) is not None:
                    for v, w in graph.get(node):
                        heapq.heappush(hp, (time+w, v))
        mx = max(elapsedTime)
        return mx if mx < 2**31-1 else -1
