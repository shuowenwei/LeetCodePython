# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-peak-element/

https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution
LC162, LC153
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
        while left < right - 1: # must ensure nums[mid +- 1] not out of index 
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid 
            elif nums[mid] < nums[mid+1]:
                left = mid + 1 
            else:
                right = mid - 1
        #handle condition 1 and 2
        return left if nums[left] >= nums[right] else right
    
    
        # solution 2: O(n), for loop
        if len(nums) <= 2:
            return nums.index(max(nums))
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i 
        if nums[0] > nums[1]:
            return 0 
        else:
            return len(nums) - 1
        
        # Solution 3: or just try to find the max number
        return nums.index(max(nums))