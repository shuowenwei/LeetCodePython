# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-paths/

backtracking
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def backtrack(node, path):
            # if node is None:
            #     return
            if node.left is None and node.right is None: # this is leaf
                res.append('->'.join(path))
                return
            if node.left:
                path.append(str(node.left.val))
                backtrack(node.left, path)
                path.pop()
            if node.right:
                path.append(str(node.right.val))
                backtrack(node.right, path)
                path.pop()
                
        backtrack(root, [str(root.val)])
        return res 
