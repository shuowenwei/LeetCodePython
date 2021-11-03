# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-level-order-traversal/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        res = []
        if root is None:
            return res
        
        q.append(root)
        while len(q) > 0: 
            size = len(q)
            tmp = []
            for i in range(size):
                cur = q.pop(0)
                tmp.append(cur.val)
                if cur.left is not None: 
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            res.append(tmp)    
        return res 