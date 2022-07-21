# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

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
        slow = 0 
        fast = 0
        count = 0 
        while fast < n:
            if nums[fast] != nums[slow]:
                # when encounter different element
                slow += 1
                nums[slow] = nums[fast]
            elif slow < fast and count < 2:
                # // 当一个元素重复次数不到 2 次时，也Ok
                slow += 1
                nums[slow] = nums[fast]
            count += 1
            fast += 1
            if fast < n and nums[fast] != nums[fast-1]:
                # // 遇到不同的元素, reset count to 0
                count = 0 
        return slow + 1
    
        # solution 2: 
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/632374/Easy-Python-solution
        n = len(nums)
        if n < 3:
            return n
        
        i , j = 1, 2
        while j < n:
            if nums[i-1] != nums[j]:
                i += 1    
            nums[i] = nums[j]
            j+= 1
        return i+1