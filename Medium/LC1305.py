# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

MG: https://www.1point3acres.com/bbs/thread-841626-1-1.html

LC1305, LC173, LC21
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def traverse(root, res):
            if root is None:
                return 
            traverse(root.left, res)
            res.append(root.val)
            traverse(root.right, res)
        res1, res2 = [], []
        traverse(root1, res1)
        traverse(root2, res2)
        p1, p2 = 0, 0
        res = []
        while p1 < len(res1) and p2 < len(res2):
            if res1[p1] < res2[p2]:
                res.append(res1[p1])
                p1 += 1
            else:
                res.append(res2[p2])
                p2 += 1
        if p1 < len(res1):
            res += res1[p1:]
        if p2 < len(res2):
            res += res2[p2:]
        return res
