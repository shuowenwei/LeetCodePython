# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/flip-equivalent-binary-trees/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if None in (root1, root2):
            return root1 == root2
        
        if root1.val != root2.val:
            return False 
        
        return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left) or self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
