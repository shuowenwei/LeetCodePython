# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-maximum-path-sum/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """     
        import sys
        self.res = -sys.maxsize 
        def dfs(node):
            if node is None:
                return 0 
            leftVal = max(dfs(node.left), 0) 
            rightVal =  max(dfs(node.right), 0)
            cur = node.val + leftVal + rightVal
            self.res = max(self.res, cur)
            return node.val + max(leftVal, rightVal)
        
        if root is None:
            return self.res
        dfs(root)
        return self.res