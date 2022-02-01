# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/diameter-of-binary-tree/

a good solution: https://www.youtube.com/watch?v=0VnOfu2pYTo 

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
        res = [0] # any two nodes (not necessarily pass through root)
        def traverse(node):
            if node is None:
                return 0
            leftLength = traverse(node.left)
            rightLength = traverse(node.right)
            res[0] = max(res[0], leftLength + rightLength)
            return 1 + max(leftLength, rightLength)
        
        _ = traverse(root)
        return res[0]
                
                
