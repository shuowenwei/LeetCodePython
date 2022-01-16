# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

https://labuladong.gitee.io/algo/4/30/117/

LC172, LC793, LC204, LC372, LC268
"""
class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        # y = f(x) is a monotonic increasing function  
        def getTrailingZeros(n):
            totalFives = 0 
            while n > 0: 
                n = n / 5
                totalFives += n
            return totalFives
        left, right = 0, 2**64-1 # sincek <= 10^9, right should be long integer's LONG_MAX
        # print(getTrailingZeros(right), getTrailingZeros(right)>10**9)
        # /* 搜索 trailingZeroes(n) == K 的左侧边界 */
        while left < right:
            mid = left + (right-left)/2
            if getTrailingZeros(mid) < k:
                left = mid + 1
            elif getTrailingZeros(mid) > k:
                right = mid 
            else:
                right = mid  
        leftBound = left 
        # /* 搜索 trailingZeroes(n) == K 的右侧边界 */
        left, right = 0, 2**64-1
        while left < right:
            mid = left + (right-left)/2
            if getTrailingZeros(mid) < k:
                left = mid + 1
            elif getTrailingZeros(mid) > k:
                right = mid 
            else:
                left = mid+1
        rightBound = left - 1
        
        return rightBound - leftBound + 1