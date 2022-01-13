# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/gas-station/

https://labuladong.gitee.io/algo/3/27/106/

LC134
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        runningSum, minSum = 0, 0
        start = 0
        for i in range(n):
            runningSum += gas[i] - cost[i]
            if runningSum < minSum:
                start = i + 1 
                minSum = runningSum
        if runningSum < 0:
            return -1 
        return start if start!=n else 0