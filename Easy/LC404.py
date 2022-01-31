# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sum-of-left-leaves/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res_left_leaves = []
        def traverse(node):
            if node is None:
                return
            if node.left and node.left.left is None and node.left.right is None:
                res_left_leaves.append(node.left.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return sum(res_left_leaves)
                
        """
        if root is None: 
            return 0 
        if root.left is None and root.right is None:
            return 0 
        queue = collections.deque()
        queue.append(root)
        leftNode = [] 
        # rightNode = [] 
        while queue:
            temp = queue.popleft()
            if temp.left:
                queue.append(temp.left)
                leftNode.append(temp.left)
            if temp.right:
                queue.append(temp.right)
                # rightNode.append(temp)
        res = 0 
        for leaf in leftNode: 
            if leaf.left is None and leaf.right is None: 
                res += leaf.val 
        return res 
        """
                
