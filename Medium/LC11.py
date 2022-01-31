# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/container-with-most-water/ 

https://labuladong.gitee.io/algo/4/32/136/

LC42, LC11, LC407
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            res = max(res, min(height[left], height[right])*(right-left))
            # 要移动较低的一边：
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res 
