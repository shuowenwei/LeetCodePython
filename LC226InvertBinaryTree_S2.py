# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/invert-binary-tree/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None 

        swapNodes(root)
        return root

def swapNodes(root):
    if root is None:
        return None 

    root.left, root.right = root.right, root.left

    swapNodes(root.left)
    swapNodes(root.right)