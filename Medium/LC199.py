# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-right-side-view/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res 
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if i == size - 1:
                    res.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
        return res 
    
        # dfs: traverse right first, save extra storage space
        res = []
        self.max_level = -1 
        def traverse_dfs(node, level):
            if node is None:
                return 
            if level > self.max_level:
                res.append(node.val)
                self.max_level = level
            # right first, for right size view 
            traverse_dfs(node.right, level + 1)
            traverse_dfs(node.left, level + 1)
            
        traverse_dfs(root, 0)
        return res 