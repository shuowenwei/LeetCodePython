# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        re = []
        curr = [root] 
        
        while curr:
            nextLevel = [] # store nodes 
            valList = []   # store nodes' value 
            for a in curr:
                valList.append(a.val)
                if a.left:
                    nextLevel.append(a.left)
                if a.right:
                    nextLevel.append(a.right)
                    
            re.append(valList)
            curr = nextLevel

        return re[::-1]