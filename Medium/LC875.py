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
        def f(piles, x): # 注意f(x)是单调递减的
            hours = 0
            for p in piles: 
                hours += p / x
                if p%x > 0: 
                    hours += 1
            return hours 

        left = 1
        right = 10**9+1 
        while left < right: 
            mid = left + (right-left)/2 
            if f(piles, mid) == h:
                right = mid 
            elif f(piles, mid) < h:
                right = mid 
            else:
                left = mid + 1 
        return left 
    
        
