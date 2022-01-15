# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

https://labuladong.gitee.io/algo/2/18/28/

LC95, LC96, LC1373
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = [0]
        def traversePostOrder(root):
            isBST = True
            rootSum = 0
            maxNodes = -2**31-1
            minNodes = 2**31+1
            if root is None: 
                return isBST, rootSum, maxNodes, minNodes
            isBST_left, rootSum_left, maxNodes_left, minNodes_left = traversePostOrder(root.left)
            isBST_right, rootSum_right, maxNodes_right, minNodes_right = traversePostOrder(root.right)
            # post order, what does this node need to do? 
            # both left and right subtree are BST
            # this node's value must > max value of the left subtree
            # this node's value must < min value of the right subtree
            if isBST_left and isBST_right and root.val > maxNodes_left and root.val < minNodes_right:
                rootSum = rootSum_left + rootSum_right + root.val
                res.append(rootSum)
                maxNodes = max(maxNodes_right, root.val) #? 
                minNodes = min(minNodes_left, root.val) #? 
                return isBST, rootSum, maxNodes, minNodes
            else:
                isBST = False
                return isBST, rootSum, maxNodes, minNodes
        isBST, rootSum, maxNodes, minNodes = traversePostOrder(root)
        return max(res)
    
