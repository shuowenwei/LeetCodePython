# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

LC863, Burning Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        dictNode2Parent = {} 
        def traverse(node, parent):
            if node is None:
                return 
            dictNode2Parent[node] = parent
            traverse(node.left, node)
            traverse(node.right, node)
        traverse(root, None)
        
        res = []
        import collections 
        visited = set([target])
        q = collections.deque()
        q.append((target, k))
        while q:
            size = len(q)
            for _ in range(size):
                cur_node, cur_k = q.popleft()
                if cur_k == 0:
                    res.append(cur_node.val)
                if cur_k < 0:
                    return res 
                if cur_node.left and cur_node.left not in visited:
                    q.append((cur_node.left, cur_k-1)) 
                    visited.add(cur_node.left)
                if cur_node.right and cur_node.right not in visited:
                    q.append((cur_node.right, cur_k-1)) 
                    visited.add(cur_node.right)
                if dictNode2Parent[cur_node] and dictNode2Parent[cur_node] not in visited:
                    q.append((dictNode2Parent[cur_node], cur_k-1))
                    visited.add(dictNode2Parent[cur_node])
        return res 

                
