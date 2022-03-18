# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-bottom-left-tree-value/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.max_depth = -1
        def traverse_dfs(node, depth):
            if node is None:
                return 
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = node.val
            traverse_dfs(node.left, depth + 1)
            traverse_dfs(node.right, depth + 1)

        traverse_dfs(root, 0)
        return self.res            
