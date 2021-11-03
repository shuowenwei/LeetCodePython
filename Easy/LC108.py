# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        midIndex = len(nums) // 2
        root = TreeNode(nums[midIndex])
        root.left = self.sortedArrayToBST(nums[:midIndex])
        root.right = self.sortedArrayToBST(nums[midIndex+1:])
        return root 
    