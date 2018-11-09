# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/intersection-of-two-arrays/

"""
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return [] 
        res = []
        """
        for n1 in nums1:
            if n1 in nums2 and n1 not in res:
                res.append(n1)
        """
        for n1 in set(nums1):
            if n1 in set(nums2):
                res.append(n1)
        return res 
        