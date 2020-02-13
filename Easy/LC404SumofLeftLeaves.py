# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sum-of-left-leaves/

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def sumOfLeftLeaves(self, root: TreeNode) -> int: 
        if not root: 
            return 0 
        # root.left is a left leaf 
        if root.left and root.left.left is None and root.left.right is None: 
            return root.left.val + self.sumOfLeftLeaves(root.right)
        # root.left is a not left leaf 
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) 
        
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
                
