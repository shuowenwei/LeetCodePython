# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/next-permutation/

https://leetcode.com/problems/next-permutation/discuss/1179544/Python-Solution-with-easy-understanding-and-comments.-(Bonus%3A-Related-links)

https://leetcode.com/problems/next-permutation/discuss/13994/Readable-code-without-confusing-ij-and-with-explanation

https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        print('i ', i)
        if i == 0: # nums are in descending order
            nums.reverse()
            return
        # If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1 
        print('k ', k, 'j ', j)
        nums[j], nums[k] = nums[k], nums[j]
        # sequence strating from i to end
        left, right = i, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1