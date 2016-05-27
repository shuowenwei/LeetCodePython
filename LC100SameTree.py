# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/same-tree/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
            
        if (p is None and q is not None) or (p is not None and q is None):
            return False 
            
        if p is not None and q is not None: 
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)