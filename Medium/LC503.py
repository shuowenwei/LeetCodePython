# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/next-greater-element-ii/

https://labuladong.github.io/algo/2/21/60/

LC496, LC739, LC503
monotonic stack
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 对于这种需求，常用套路就是将数组长度翻倍：
        n = len(nums)
        nums = nums + nums
        res = [0]*2*n
        stack = []
        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            # while stack:
            #     if stack[-1] <= nums[i%n]:
            #         stack.pop()
            #     else:
            #         break
            if len(stack) == 0:
                res[i] = - 1
            else:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res[:n]