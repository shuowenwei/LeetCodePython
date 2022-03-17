# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

https://labuladong.gitee.io/algo/2/19/23/

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
        # // 先递归拉平左右子树
        self.flatten(root.left)
        self.flatten(root.right)
        
        # /****后序遍历位置****/
        # // 1、左右子树已经被拉平成一条链表
        leftTreeStartNode = root.left
        rightTreeStartNode= root.right
        
        # // 2、将左子树作为右子树
        root.left = None
        root.right = leftTreeStartNode
        
        # // 3、将原先的右子树接到当前右子树的末端
        p = root
        while p.right is not None:
            p = p.right    
        p.right = rightTreeStartNode
        
        # solution 2:
        """
        if root is None:
            return
        
        leftTreeStartNode = self.flatten(root.left)
        rightTreeStartNode = self.flatten(root.right)
        
        root.left = None
        root.right = leftTreeStartNode
        
        cur = root
        while cur.right is not None:
            cur = cur.right    
        cur.right = rightTreeStartNode
        
        return root 
        """
