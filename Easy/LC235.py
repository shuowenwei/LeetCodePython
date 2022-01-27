# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

LC235, LC236
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
            return root # None or p or q exists in the tree? 
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        
    # solutiono 2: refer to LC236 directly
    """ 
        if root in (None, p, q):
            return root # None or p or q exists in the tree? 
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        # do sth in post order
        if leftLCA and rightLCA:
            return root
        elif leftLCA and rightLCA is None:
            return leftLCA 
        elif leftLCA is None and rightLCA:
            return rightLCA
        else: # both leftLCA and rightLCA are None
            return None #leftLCA or rightLCA
    """