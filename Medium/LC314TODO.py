# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-vertical-order-traversal/

https://www.techiedelight.com/vertical-traversal-binary-tree/

LC314, LC987
Meta VO
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        # solution 1: DFS
        res = []
        def traverse_DFS(node, verticalOrder, horizontalOrder):
            if node is None:
                return 
            res.append(node.val, verticalOrder, horizontalOrder)
            traverse(node.left, verticalOrder - 1, horizontalOrder + 1)
            traverse(node.right, verticalOrder + 1, horizontalOrder + 1)
        traverse(root, 0, 0)
        res.sort(key = lambda x : (x[1], x[2], x[0]))
        # print(dict_order)
        return [a[0] for a in res ]

        # solution 2: BFS
        dict_order = collections.defaultdict(list)
        q = collections.deque()
        q.append((root, 0))
        while q:
            size = len(q)
            for i in range(size):
                node, verticalOrder = q.popleft()
                dict_order[verticalOrder].append(node.val)
                if node.left: 
                    q.append((node.left, verticalOrder - 1))
                if node.right:
                    q.append((node.right, verticalOrder + 1))
        print(dict_order)
        return root