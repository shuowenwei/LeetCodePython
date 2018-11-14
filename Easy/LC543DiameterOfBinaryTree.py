# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/diameter-of-binary-tree/

a good solution: https://www.youtube.com/watch?v=0VnOfu2pYTo 

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0 
        def DFS(node):
            if node is None:
                return 0 
            leftLength = DFS(node.left)
            rightLength = DFS(node.right)
            self.res = max(self.res, leftLength + rightLength)
            return max(leftLength, rightLength) + 1
        DFS(root)
        return self.res 
                
