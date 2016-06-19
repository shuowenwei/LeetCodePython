# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) <= len(nums2):
            for a in nums1: 
                if a in nums2: 
                    nums2.remove(a)
                    res.append(a)
        else:
            for a in nums2:
                if a in nums1:
                    nums1.remove(a)
                    res.append(a)
        return res
