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
            length = right - left
            res = max(res, min(height[left], height[right]) * length )
            # 要移动较低的一边：
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res 


        # solution 2: refer to LC42: two pointers
        res = 0 
        if not height:
            return res 
        left, right = 0, len(height) - 1 
        leftMax, rightMax = 0, 0 
        # leftMax 和 rightMax 代表的 是 height[0..left] 和 height[right..end] 的最高柱子高度
        while left < right:
            length = right - left
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax <= rightMax:
                res = max(res, length * leftMax)
                left += 1 
            elif leftMax > rightMax:
                res = max(res, length * rightMax)
                right -= 1
        return res 