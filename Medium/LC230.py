# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

https://labuladong.gitee.io/algo/2/18/24/

LC230, LC538, LC1038

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """    
        res = []
        def traversal(root):
            if root is None:
                return
            traversal(root.left)
            res.append(root.val)
            if len(res) == k:
                return 
            traversal(root.right)
            
        traversal(root)
        return res[k-1]
        