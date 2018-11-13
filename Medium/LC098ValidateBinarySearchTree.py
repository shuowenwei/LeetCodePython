# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/validate-binary-search-tree

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    import sys
    def isValidBST(self, root, ceil = sys.maxsize, floor = -sys.maxsize):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.val >= ceil or root.val <= floor:
            return False
        return self.isValidBST(root.left, min(root.val, ceil), floor) and self.isValidBST(root.right, ceil, max(root.val, floor))
        