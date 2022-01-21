# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/trapping-rain-water/

solution: https://leetcode.com/articles/trapping-rain-water/

https://leetcode.com/problems/trapping-rain-water/discuss/17554/Share-my-one-pass-Python-solution-with-explaination

https://labuladong.gitee.io/algo/4/32/136/

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
        left, right = 0, len(height) - 1 
        leftMax, rightMax = 0, 0 
        # leftMax 和 rightMax 代表的是 height[0..left] 和 height[right..end] 的最高柱子高度
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax <= rightMax:
                res += leftMax - height[left]
                left += 1 
            elif leftMax > rightMax:
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
        # my solution: 所以对于这种问题，我们不要想整体，而应该去想局部；就像之前的文章写的动态规划问题处理字符串问题，不要考虑如何处理整个字符串，而是去思考应该如何处理每一个字符。
        # 这么一想，可以发现这道题的思路其实很简单。具体来说，仅仅对于位置 i，能装下多少水呢？
        n = len(height)
        leftMax, rightMax = [0]*n, [0]*n
        
        currMax = 0
        for i in range(n):
            if height[i] > currMax:
                currMax = height[i] 
            leftMax[i] = currMax
        
        currMax = 0 
        for j in range(n-1, -1, -1):
            if height[j] > currMax:
                currMax = height[j] 
            rightMax[j] = currMax
        
        res = 0 
        # print(leftMax)
        # print(rightMax)
        for i in range(n):
            res += max(0, min(leftMax[i], rightMax[i]) - height[i]) 
            # can't holdn negative amount of water
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