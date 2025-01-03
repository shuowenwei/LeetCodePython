# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-sorted-array/

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
        """
        if n == 0:
            return nums1 
        nums1_sz = len(nums1)
        for i in range(nums1_sz-1, -1, -1):
            if m > 0 and n > 0:
                if nums1[m-1] < nums2[n-1]:
                    nums1[i] = nums2[n-1]
                    n -= 1
                else: 
                    nums1[i] = nums1[m-1]
                    m -= 1
                continue
            if m > 0:
                nums1[i] = nums1[m-1]
                m -= 1
            if n > 0:
                nums1[i] = nums2[n-1]
                n -= 1
        """