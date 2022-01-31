# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-leaves-of-binary-tree/

"""
# Binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        res = []
        def dfs(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                res.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return res 
        