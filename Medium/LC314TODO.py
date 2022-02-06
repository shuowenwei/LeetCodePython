# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-vertical-order-traversal/

https://www.techiedelight.com/vertical-traversal-binary-tree/

LC314, LC987
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
        dict_order = collections.defaultdict(list)
        def traverse(node, verticalOrder):
            if node is None:
                return 
            dict_order[verticalOrder].append(node.val)
            traverse(node.left, verticalOrder - 1)
            traverse(node.right, verticalOrder + 1)
        traverse(root, 0)
        # print(dict_order)
        return dict_order

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