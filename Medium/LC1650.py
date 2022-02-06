# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

LC235, LC236, LC1650
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        root = p
        while root.parent != None:
            root = root.parent
        
        # refer to KC235
        def helper(root, p, q):
            if root in (None, p, q):
                return root # None or p or q exists in the tree? 
            leftLCA = self.helper(root.left, p, q)
            rightLCA = self.helper(root.right, p, q)
            # do sth in post order
            if leftLCA and rightLCA:
                return root
            elif leftLCA: # and rightLCA is None:
                return leftLCA 
            elif rightLCA: # and leftLCA is None:
                return rightLCA
            else: # both leftLCA and rightLCA are None
                return None #leftLCA or rightLCA
            
        return helper(root, p, q)
    