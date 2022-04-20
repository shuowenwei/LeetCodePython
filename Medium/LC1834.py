# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-threaded-cpu/

https://leetcode.com/problems/single-threaded-cpu/discuss/1163980/Python-Sort-then-Heap

LC1834, LC2050, LC630, LC636
"""
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        tasks_index = [(t[0], t[1], index) for index, t in enumerate(tasks)]
        tasks_index.sort(key = lambda x: [x[0], x[2]])
        
        from heapq import heappush, heappop
        res = []
        hp = []
        pointer = 0 
        cur_time = tasks_index[pointer][0] # earliest task to enter queue 
        while len(res) < len(tasks_index): # break when all tasks are processed 
            # push all tasks with enter_time <= cur_time, when picking the shortest on to start
            while pointer < len(tasks_index) and cur_time >= tasks_index[pointer][0]:
                enter, processtime, index = tasks_index[pointer]
                heappush(hp, (processtime, index))
                pointer += 1
                
            if hp:
                processtime, index = heappop(hp)
                cur_time += processtime
                res.append(index)
            elif pointer < len(tasks_index):
                cur_time = tasks_index[pointer][0]
        return res 
