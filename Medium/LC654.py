# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-binary-tree/

https://labuladong.gitee.io/algo/2/18/22/

LC654, LC105, LC106 

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