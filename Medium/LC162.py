# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-peak-element/

https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution

"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return nums.index(max(nums))
 # if an element(not the right-most one) is smaller than its right neighbor, 
 # then there must be a peak element on its right, because the elements on its right is either 
 #   1. always increasing  -> the right-most element is the peak
 #   2. always decreasing  -> the left-most element is the peak
 #   3. first increasing then decreasing -> the pivot point is the peak
 #   4. first decreasing then increasing -> the left-most element is the peak  
 # Therefore, we can find the peak only on its right elements( cut the array to half)
 # The same idea applies to that an element(not the left-most one) is smaller than its left neighbor.
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid 
            elif nums[mid] < nums[mid+1]:
                left = mid + 1 
            else:
                right = mid - 1
        return left if nums[left] >= nums[right] else right