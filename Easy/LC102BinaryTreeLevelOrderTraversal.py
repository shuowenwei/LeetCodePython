# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-level-order-traversal/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return [] 
        currentLevel = [root]
        returnVal = [[root.val]]
        while currentLevel: 
            nextLevel = [] 
            for n in currentLevel:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            if nextLevel:
                returnVal.append([i.val for i in nextLevel])    
            currentLevel = nextLevel
            
        return returnVal
        