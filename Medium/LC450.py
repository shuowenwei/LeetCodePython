# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/delete-node-in-a-bst/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None 

        if root.val == key:
            if root.left is None and root.right is None:
                return None 
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else: # root.left is not None and root.right is not None:
                # First find the right most leaf of the left sub-tree
                leftSubTree_mostRight = root.left 
                while leftSubTree_mostRight.right:
                    leftSubTree_mostRight = leftSubTree_mostRight.right
                # Attach right child to the right of that leaf
                leftSubTree_mostRight.right = root.right
                # Return left child instead of root, a.k.a delete root
                return root.left
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root