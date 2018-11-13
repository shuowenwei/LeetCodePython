# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
one solution: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root 
        left_kids =  self.lowestCommonAncestor(root.left, p, q)
        right_kids =  self.lowestCommonAncestor(root.right, p, q)
        
        if left_kids is not None and right_kids is not None:
            return root 
        if left_kids is None and right_kids is not None: 
            return right_kids
        if left_kids is not None and right_kids is None: 
            return left_kids
        
