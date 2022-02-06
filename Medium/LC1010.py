# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

"""
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        time_reminder = [t % 60 for t in time]
        res = 0 
        dict_time = collections.defaultdict(list)
        for i in range(len(time_reminder)):
            tmp = (60 - time_reminder[i]) % 60
            if tmp in dict_time:
                res += len(dict_time[tmp])
            dict_time[time_reminder[i]].append(i)
        # print(dict_time)
        return res 
