# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/symmetric-tree/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True 
        return self.isSameTree(root.left, root.right)
        
    def isSameTree(self, left, right): 
        """
        rType: bool 
        """
        if left is None and right is None:
            return True
        if (left is not None and right is None) or (left is None and right is not None):
            return False
        if left.val != right.val: 
            return False
        else:
            return self.isSameTree(left.left, right.right) and self.isSameTree(left.right, right.left)
        
        