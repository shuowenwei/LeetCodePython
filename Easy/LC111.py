# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/

https://labuladong.gitee.io/algo/4/29/113/

LC111, LC752, LC773
- BFS
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS: 
        if root is None:
            return 0
        from collections import deque
        q = deque()
        q.append(root)
        height = 1 
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr.left is None and curr.right is None:
                    return height 
                if curr.left is not None: 
                    q.append(curr.left)
                if curr.right is not None: 
                    q.append(curr.right)
            height += 1 
        return height
    
        # solution 2: DFS - not a good choice 
        if root is None:
            return 0
        if None in (root.left, root.right): # DFS is bad choice here
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
