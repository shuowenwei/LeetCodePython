# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-binary-tree/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None 
        maxVal = max(nums)
        maxVal_index = nums.index(maxVal)
        root = TreeNode(maxVal)
        root.left = self.constructMaximumBinaryTree(nums[:maxVal_index])
        root.right = self.constructMaximumBinaryTree(nums[maxVal_index+1:])
        return root 