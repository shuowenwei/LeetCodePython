# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

https://labuladong.gitee.io/algo/2/18/21/

LC226, LC114, LC116

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        leftTreeStartNode = root.left
        rightTreeStartNode= root.right
        
        root.left = None
        root.right = leftTreeStartNode
        
        p = root
        while p.right is not None:
            p = p.right    
        p.right = rightTreeStartNode
        