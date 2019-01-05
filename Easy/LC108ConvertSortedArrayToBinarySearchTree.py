# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """ 
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])        
        mid = len(nums)//2
        root = TreeNode(nums[mid]) 
        leftNums = nums[:mid]
        rightNums = nums[mid+1:]
        root.left = self.sortedArrayToBST(leftNums)
        root.right = self.sortedArrayToBST(rightNums)
        return root 
    