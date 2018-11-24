# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/container-with-most-water/ 

solution: https://leetcode.com/problems/container-with-most-water/solution/

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0 
        left = 0
        right = len(height) - 1 
        while left < right:
            if min(height[left], height[right])*(right - left) > maxarea: 
                maxarea = min(height[left], height[right]) * (right - left)
            if height[left] >= height[right]: 
                right -= 1
            else:
                left += 1 
        return maxarea 
