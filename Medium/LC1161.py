# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        from collections import deque 
        q = deque()
        level = 0
        levelSum = 0
        q.append(root)
        while q:
            size = len(q)
            level += 1
            levelSum = 0 
            for i in range(size):
                cur = q.popleft()
                levelSum += cur.val 
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append((level, levelSum))
        res.sort(key=lambda x: (-x[1], x[0]))
        # print(res)
        return res[0][0]
