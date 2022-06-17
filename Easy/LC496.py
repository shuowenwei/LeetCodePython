# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/next-greater-element-i/

https://labuladong.gitee.io/algo/2/20/48/

LC496, LC739, LC503
monotonic stack
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # All integers in nums1 and nums2 are unique.
        dctNum1toIndex = dict() # num1's number' next greater number's index in nums2
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            cur = nums2[i]
            while stack and stack[-1] <= cur:
                stack.pop()
            # while stack:
            #     if stack[-1] <= cur:
            #         stack.pop()
            #     else:
            #         break
            if len(stack) == 0:
                dctNum1toIndex[cur] = - 1
            else:
                dctNum1toIndex[cur] = stack[-1]
            stack.append(cur)
        
        # All the integers of nums1 also appear in nums2.
        return [dctNum1toIndex[n] for n in nums1]
            
