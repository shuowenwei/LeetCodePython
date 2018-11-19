# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-paths/

solution: https://leetcode.com/problems/binary-tree-paths/discuss/68272/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively). 

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
        """   #  dfs Recursivly 
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, node, path, res):
        if node is None:
            return
        if node.left is None and node.right is None: # this is leaf 
            res.append("{}{}".format(path, node.val))
        if node.left is not None:
            self.dfs(node.left, "{}{}->".format(path, node.val), res)
        if node.right is not None:
            self.dfs(node.right, "{}{}->".format(path, node.val), res)
            
        """ dfs + stack 
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if node is None:
                continue
            if node.left is None and node.right is None: # this is the leaf nonde 
                res.append("{}{}".format(path,node.val))
            if node.left is not None:
                stack.append((node.left, "{}{}->".format(path,node.val)))
            if node.right is not None: 
                stack.append((node.right, "{}{}->".format(path,node.val)))
        return res
        """