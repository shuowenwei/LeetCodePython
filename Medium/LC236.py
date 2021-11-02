# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
one solution: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C%2B%2BJavaPythonRuby 
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root # None or p or q exists in the tree? 
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        
        if leftLCA is not None and rightLCA is not None:
            return root
        # elif leftLCA is not None and rightLCA is None:
        #     return leftLCA 
        # elif leftLCA is None and rightLCA is not None:
        #     return rightLCA
        else:
            return leftLCA or rightLCA
"""
        # Solution 2: Time Limit Exceeded
        # help function 
        def isInTree(root, nodeVal):
            if root is None:
                return False 
            elif root is nodeVal:
                return True
            else:
                return isInTree(root.left, nodeVal) or isInTree(root.right, nodeVal)
            
        if isInTree(root.left, p) and isInTree(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif isInTree(root.right, p) and isInTree(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
"""

        
