# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-duplicate-subtrees/

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
        res = []
        if root is None:
            return res
        
        hashMap = {}
        def serializeTree(root):
            if root is None:
                return '#'
            left = serializeTree(root.left)
            right = serializeTree(root.right)
            # TODOs in postorder 
            root_string = left + ',' + right + ',' + str(root.val)
                
            if root_string in hashMap:
                hashMap[root_string] += 1 
                if hashMap[root_string] == 1: 
                    res.append(root)
            else:
                hashMap[root_string] = 0
            return root_string

        root_string = serializeTree(root)
        return res 
        
        
        