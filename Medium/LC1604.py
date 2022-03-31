# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

"""
class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        dctName2Times = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hour, minute = time.split(':')
            dctName2Times[name].append(60*int(hour) + int(minute))
        
        res = []
        for name, lstTime in dctName2Times.items():
            if len(lstTime) <= 2:
                continue
            lstTime.sort()
            for i in range(len(lstTime) - 2):
                if lstTime[i+2] - lstTime[i] <= 60:
                    res.append(name)
                    break 
        return sorted(res)
