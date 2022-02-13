# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-maximum-path-sum/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [-2**32]
        def traverse(node):
            if node is None:
                return 0 
            leftMaxVal = max(traverse(node.left), 0)
            rightMaxVal = max(traverse(node.right), 0) 
            # postorder operation
            res[0] = max(res[0], node.val + leftMaxVal + rightMaxVal) 
            return node.val + max(leftMaxVal, rightMaxVal)
        
        traverse(root)
        return res[0]