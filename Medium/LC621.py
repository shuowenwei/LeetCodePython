# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/task-scheduler

reference: https://www.youtube.com/watch?v=YCD_iYxyXoo

"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = collections.defaultdict(int)
        max_freq = 0
        for t in tasks:
            freq[t] += 1
            max_freq = max(max_freq, freq[t])
            
        num_max_freq = freq.values().count(max_freq)
        
        # tasks = ["A","A","A","B","B","B"], n = 2
        # A -> B -> idle -> A -> B -> idle -> A -> B
        return max(len(tasks), (max_freq-1)*n + max_freq + num_max_freq - 1)
                