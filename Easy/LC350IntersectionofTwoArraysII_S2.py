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
        nums1.sort()
        nums2.sort()
        res = []
        if len(nums1) == 0 or len(nums2) == 0:
            return res
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2): 
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j +=1
            elif nums1[i] < nums2[j]:
                i += 1
            else: 
                j += 1
        return res
        