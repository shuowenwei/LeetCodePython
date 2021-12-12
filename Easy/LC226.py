# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/invert-binary-tree/

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
        """ # solution: postorder recursion 
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
        """
        # solution, get preOrder list ? 
        if root is None:
            return
        
        preOrder = []
        def traverse(root):
            if root is None:
                return 
            preOrder.append(root.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        if len(preOrder) <= 1:
            return 
        root.left = None 
        p = root 
        for val in preOrder[1:]: 
            p.right = TreeNode(val)
            p = p.right 
        