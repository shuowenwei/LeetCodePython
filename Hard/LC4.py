# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/median-of-two-sorted-arrays/

https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation

"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n: # always make m is smaller than n
            return self.findMedianSortedArrays(nums2, nums1)

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        # left_part          |        right_part
        # A[0], A[1], ..., 2(A[i-1])  |  1(A[i]), A[i+1], ..., A[m-1] # compare 1()
        # B[0], B[1], ..., 1(B[j-1])  |  2(B[j]), B[j+1], ..., B[n-1] # compare 2()
        while imin <= imax: 
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it 
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # i is too big, must decrease it 
                imax = i - 1
            else:
                # i is perfect 
                if i == 0: max_of_left = nums2[j-1] # num1[-1] does not exist
                elif j == 0: max_of_left = nums1[i-1] # num2[-1] does not exist
                else: max_of_left = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return max_of_left
                
                if i == m: min_of_right = nums2[j] # num1[m] does not exist
                elif j == n: min_of_right = nums1[i] # num2[n] does not exist
                else: min_of_right = min(nums1[i], nums2[j])
                    
                return (max_of_left + min_of_right) / 2.0 
            

