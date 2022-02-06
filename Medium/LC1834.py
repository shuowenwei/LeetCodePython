# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-threaded-cpu/

https://leetcode.com/problems/single-threaded-cpu/discuss/1163980/Python-Sort-then-Heap

LC1834, LC2050, LC630
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
        process_index = 0 
        cur_time = tasks_index[process_index][0] # earliest task to enter queue 
        while len(res) < len(tasks_index): # break when all tasks are processed 
            # push all tasks with enter_time <= cur_time, when picking the shortest on to start
            while process_index < len(tasks_index) and tasks_index[process_index][0] <= cur_time:
                enter, processtime, index = tasks_index[process_index]
                heappush(hp, (processtime, index))
                process_index += 1
            if hp:
                processtime, index = heappop(hp)
                cur_time += processtime
                res.append(index)
            elif process_index < len(tasks_index):
                cur_time = tasks_index[process_index][0]
        return res 
