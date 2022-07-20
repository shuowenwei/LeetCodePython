# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/path-sum/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, targetSum):
            if node is None:
                return False
            elif targetSum == node.val and node.left is None and node.right is None:
                return True
            else:
                return dfs(node.left, targetSum - node.val) or dfs(node.right, targetSum - node.val)
        
        return dfs(root, targetSum)

        # def dfs(node, targetSum, curSum):
        #     if node is None:
        #         return False
        #     elif targetSum == curSum and node.left is None and node.right is None:
        #         return True
        #     else:
        #         print(targetSum, curSum, node.val)
        #         return dfs(node.left, targetSum, curSum + node.val) or dfs(node.right, targetSum, curSum + node.val)
        
        # return dfs(root, targetSum, 0)
