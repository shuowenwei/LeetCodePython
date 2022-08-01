# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-preorder-traversal/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # solution 1: 
        res = []        
        def preorderTraverse(root):
            if root is None:
                return          
            res.append(root.val)
            preorderTraverse(root.left)
            preorderTraverse(root.right)
        preorderTraverse(root)
        return res 
    

        # solution 2: recursively
        """
        res = []
        if root is None:
            return res         
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res 
        """