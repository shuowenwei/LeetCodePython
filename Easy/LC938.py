# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/range-sum-of-bst/

https://leetcode.com/problems/range-sum-of-bst/discuss/409173/Clean-and-fast(94)-4-line-Python3-code

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        res = []
        def traverse(root, low, high):
            if root is None:
                return
            if root.val < low:
                traverse(root.right, low, high)
            elif root.val > high:
                traverse(root.left, low, high)
            else:
                res.append(root.val)
                traverse(root.left, low, high)
                traverse(root.right, low, high)
        traverse(root, low, high)
        return sum(res)
        
        # or 
        res = []
        def traverse(node, low, high):
            if node is None:
                return 
            if low <= node.val <= high:
                res.append(node.val)
            traverse(node.left, low, high)
            traverse(node.right, low, high)
        traverse(root, low, high)
        return sum(res) 


        # faster: https://leetcode.com/problems/range-sum-of-bst/discuss/409173/Clean-and-fast(94)-4-line-Python3-code
        def traverse(node, low, high):
            if node is None:
                return 0
            if low <= node.val <= high:
                return node.val + traverse(node.left, low, high) + traverse(node.right, low, high)
            elif node.val < low:
                return traverse(node.right, low, high)
            elif node.val > high:
                return traverse(node.left, low, high)
        return traverse(root, low, high)
    
        # simpler and clenaer
        if root is None:
            return 0 
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)