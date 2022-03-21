# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

LC875, LC1011, lC1891
"""
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        # this is monotonic decreasing 
        def getDays(weights, weight_cap):
            cur_carry = 0
            daysNeeded = 1 # this must start with 1!!!!!!
            for w in weights:
                if cur_carry + w <= weight_cap:
                    cur_carry += w
                else: # >
                    cur_carry = w
                    daysNeeded += 1
            return daysNeeded
        
        left, right = max(weights) , sum(weights)
        while left <= right:
            mid_cap = left + (right - left) // 2
            required_days = getDays(weights, mid_cap)
            # print(required_days, left, mid, right)
            if required_days < days:
                # // 需要让 f(x) 的返回值大一些，减少capacity
                right = mid - 1
            elif required_days > days:
                # // 需要让 f(x) 的返回值小一些，增加capacity
                left = mid + 1
            elif required_days == days:
                # // 搜索左侧边界，则需要收缩右侧边界
                right = mid - 1
        return left # or: right + 1
