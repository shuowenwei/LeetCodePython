# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = [0]
        def traverseTree(root):
            if root is None:
                return 0
            traverseTree(root.right)
            root.val += res[-1]
            res.append(root.val)
            traverseTree(root.left)
            
        traverseTree(root)
        return root 