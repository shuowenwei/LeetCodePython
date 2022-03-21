# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/diameter-of-binary-tree/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0 
        def traverse(node):
            if node is None:
                return 0
            leftLength = traverse(node.left)
            rightLength = traverse(node.right)
            self.res = max(self.res, leftLength + rightLength)
            return 1 + max(leftLength, rightLength)
        
        _ = traverse(root)
        return self.res
                
                
