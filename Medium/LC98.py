# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/validate-binary-search-tree

https://labuladong.gitee.io/algo/2/18/25/

LC450, LC701, LC700, LC98

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # solution 1: use inorder of BST is sorted
        inorder = []
        def traverseInorder(root):
            if root is None:
                return
            traverseInorder(root.left)
            inorder.append(root.val)
            traverseInorder(root.right)
            
        traverseInorder(root)
        print(inorder)
        for i in range(len(inorder)-1): 
            if inorder[i] >= inorder[i+1]:
                return False 
        return True 

        """
        # solution 2:
        def helper(root, floor, ceil): 
            if root is None:
                return True
            if root.val <= floor or root.val >= ceil:
                return False
            if root.left and root.left.val >= root.val:
                return False 
            if root.right and root.right.val <= root.val:
                return False
            else:
                return helper(root.left, floor, min(ceil, root.val)) \
            and helper(root.right, max(floor, root.val), ceil)

        return helper(root, -2**31-1, 2**31+1)
        """
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    import sys
    def isValidBST(self, root, ceil = sys.maxsize, floor = -sys.maxsize):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.val >= ceil or root.val <= floor:
            return False
        return self.isValidBST(root.left, min(root.val, ceil), floor) and self.isValidBST(root.right, ceil, max(root.val, floor))
        

