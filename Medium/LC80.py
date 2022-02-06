# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/632374/Easy-Python-solution

LC26, LC83, LC27, LC283, LC80
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return n 
        slow = 1 
        fast = 2
        while fast < n:
            if nums[slow-1] != nums[fast]:
                slow += 1 # always keep slow moving
                
            nums[slow] = nums[fast]
            fast += 1
            
        return slow + 1
