# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/delete-nodes-and-return-forest/

refer to https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328854/Python-Recursion-with-explanation-Question-seen-in-a-2016-interview

https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaC%2B%2BPython-Recursion-Solution
If a node is root (has no parent) and isn't deleted, when will we add it to the result.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        dct_to_delete = {node for node in to_delete}
        
        res = []
        def dfs(node, is_root):
            if node is None:
                return None
            isInDelete = node.val in dct_to_delete
            if is_root is True and isInDelete is False:
                res.append(node)
            if isInDelete:
                node.left = dfs(node.left, True)
                node.right = dfs(node.right, True)
                return None
            else:
                node.left = dfs(node.left, False)
                node.right = dfs(node.right, False)
                return node
        dfs(root, True)
        return res 
            
        # more precise solution
        dct_to_delete = {node for node in to_delete}
        res = []
        def dfs(node, is_root):
            if node is None:
                return None
            isInDelete = node.val in dct_to_delete
            if is_root is True and isInDelete is False:
                res.append(node)
            node.left = dfs(node.left, isInDelete)
            node.right = dfs(node.right, isInDelete)
            return None if isInDelete else node
        dfs(root, True)
        return res 
            
        
