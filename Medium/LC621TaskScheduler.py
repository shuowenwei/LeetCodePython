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
        from collections import Counter
        tCnter = Counter(tasks)
        freq = [ [k, freq] for k, freq in tCnter.items()]
        freq.sort(key= lambda x : x[1], reverse = True)
        
        max_freq = freq[0][1]
        num_max_freq = 0
        for i in freq:
            if i[1] < max_freq:
                break
            num_max_freq += 1
        return max(len(tasks), (max_freq - 1) * (n+1) + num_max_freq)
                