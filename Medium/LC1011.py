# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

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
            num_days = 1 # this must start with 1!!!!!!
            for w in weights:
                if cur_carry + w <= weight_cap:
                    cur_carry += w
                else:
                    cur_carry = w
                    num_days += 1
            return num_days
        
        left, right = max(weights) , sum(weights)
        while left <= right:
            mid = (right + left) / 2
            required_days = getDays(weights, mid)
            # print(required_days, left, mid, right)
            if required_days < days:
                right = mid - 1
            elif required_days > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
