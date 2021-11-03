# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/symmetric-tree/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True 
        return self.isSameTree(root.left, root.right)
        
    def isSameTree(self, left, right): 
        """
        rType: bool 
        """
        if left is None and right is None:
            return True
        elif left and right and left.val == right.val:
            return self.isSameTree(left.left, right.right) and self.isSameTree(left.right, right.left)
        else:
            return False 
        
        """
        # solution 2: 
        if root is None:
            return True

        def helper(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is not None and node2 is None:
                return False 
            elif node1 is None and node2 is not None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)
            
        return helper(root.left, root.right)
        """
