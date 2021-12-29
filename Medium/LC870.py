# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/advantage-shuffle/

https://labuladong.gitee.io/algo/2/21/60/

"""
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2_sort = sorted([(n,i) for i,n in enumerate(nums2)], key=lambda x:x[0], reverse=True)
        nums1_sort = sorted(nums1, reverse=True)
        res = [0]*len(nums1)
        for n, i in nums2_sort:
            if nums1_sort[0] > n:
                res[i] = nums1_sort.pop(0)
            else:
                res[i] = nums1_sort.pop()
        return res 
