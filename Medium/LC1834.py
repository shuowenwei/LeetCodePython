# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-threaded-cpu/

https://leetcode.com/problems/single-threaded-cpu/discuss/1163980/Python-Sort-then-Heap

LC1834, LC2050
"""
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        tasks_index = [(t[0], t[1], index) for index, t in enumerate(tasks)]
        tasks_index.sort(key = lambda x: x[0])
        
        from heapq import heappush
        res = []
        hp = []
        p = 0 
        time = tasks_index[p][0] # earliest task to enter queue 
        while len(res) < len(tasks_index): # break when all tasks are processed 
            while p < len(tasks_index) and tasks_index[p][0] <= time:
                enter, processtime, index = tasks_index[p]
                heappush(hp, (processtime, index))
                p += 1
            if hp:
                processtime, index = heappop(hp)
                time += processtime
                res.append(index)
            elif p < len(tasks_index):
                time = tasks_index[p][0]
        return res 
