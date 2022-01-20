# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/koko-eating-bananas/

https://labuladong.gitee.io/algo/2/21/59/
https://mp.weixin.qq.com/s/E2cyJwMVxRosaU2-bZyTjA

LC704, LC34, LC875, LC1101, LC410
"""
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """ 
        def getHours(k):# 注意f(x)是单调递减的
            hours = 0
            for p in piles:
                hours += p / k
                if p%k != 0:
                    hours += 1
            return hours 
        
        left, right = 1, 10**9
        while left <= right: # left boundary template
            mid = left + (right-left)/2
            if getHours(mid) == h:
                right = mid - 1
            elif getHours(mid) < h:
                right = mid - 1
            elif getHours(mid) > h:
                left = mid + 1
        return left
    
        
