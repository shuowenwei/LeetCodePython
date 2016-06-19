# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-paths/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """   #  Recursive  
        """
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, node, path, res):
        if not node:
            return
        
        if not node.left and not node.right:
            res.append("{}{}".format(path, node.val))
        self.dfs(node.left, "{}{}->".format(path, node.val), res)
        self.dfs(node.right, "{}{}->".format(path, node.val), res)
        """
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node:
                continue
            if not node.left and not node.right:
                res.append("{}{}".format(path,node.val))
            stack.append((node.left, "{}{}->".format(path,node.val)))
            stack.append((node.right, "{}{}->".format(path,node.val)))
        return res