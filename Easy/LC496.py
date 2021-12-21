# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/next-greater-element-i/

https://labuladong.gitee.io/algo/2/20/48/

"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # All integers in nums1 and nums2 are unique.
        res = dict()
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                    stack.pop()

            if len(stack) == 0:
                res[nums2[i]] = - 1
            else:
                res[nums2[i]]  = stack[-1]
            stack.append(nums2[i])
        
        # All the integers of nums1 also appear in nums2.
        return [res[n] for n in nums1]
            
