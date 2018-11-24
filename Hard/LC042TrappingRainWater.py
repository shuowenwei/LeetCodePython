# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/trapping-rain-water/

solution: https://leetcode.com/articles/trapping-rain-water/

https://leetcode.com/problems/trapping-rain-water/discuss/17554/Share-my-one-pass-Python-solution-with-explaination

"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # two pointers
        res = 0 
        if not height:
            return res 
        left = 0
        right = len(height) - 1 
        leftMax = height[left]
        rightMax = height[right]
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax <= rightMax:
                res += leftMax - height[left]
                left += 1 
            if leftMax > rightMax:
                res += rightMax - height[right]
                right -= 1
        return res 
    
        """
        # use a stack https://leetcode.com/articles/trapping-rain-water/ 
        res = 0 
        stack = [] # top index's height is bounded/shorter than previous index's height 
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                #if empty after one pop, then there's no left bounded bar
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                res += distance * bounded_height
            stack.append(i)
        return res
        """ 
        
        """
        # dynamic programming
        res = 0
        if not height:
            return res 
        leftMax = [0] * len(height)
        rightMax = [0] * len(height) 
        leftMax[0] = height[0] 
        rightMax[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(height)): 
            leftMax[i] = max(leftMax[i-1], height[i])
        for j in range(len(height)-2, -1, -1): 
            rightMax[j] = max(rightMax[j+1], height[j])
        
        for k in range(len(height)):
            res += max(min(leftMax[k], rightMax[k]) - height[k], 0)
        return res 
        """
        
        
        """
        #brute force 
        res = 0 
        for i in range(len(height)):
            leftMax, rightMax = 0, 0
            for left in range(0, i):
                leftMax = max(leftMax, height[left])
            for right in range(i, len(height)):
                rightMax = max(rightMax, height[right])
            res += max(min(leftMax, rightMax) - height[i], 0) 
        return res 
        """ 