# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/average-waiting-time/

LC1071, LC
simulation
"""
class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        total_wait_time = 0 
        pre_order_finish_time = 0 
        for arrive, wait_time in customers:
            if pre_order_finish_time < arrive:
                total_wait_time += wait_time
                pre_order_finish_time = arrive + wait_time
            else:
                total_wait_time += (pre_order_finish_time + wait_time) - arrive
                pre_order_finish_time = pre_order_finish_time + wait_time
                            
        return total_wait_time/float(len(customers))
