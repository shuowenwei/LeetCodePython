# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

LC314, LC987
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dict_order = collections.defaultdict(list)
        
        # solution 1: DFS 
        def traverse(node, verticalOrder, level):
            if node is None:
                return 
            dict_order[verticalOrder].append( (level, node.val) )
            traverse(node.left, verticalOrder - 1, level + 1)
            traverse(node.right, verticalOrder + 1, level + 1)
        traverse(root, 0, 0)
        # solution 2: BFS 
        """
        q = collections.deque()
        level = 0
        verticalOrder = 0 
        q.append((root, verticalOrder, level))
        while q:
            size = len(q)
            for i in range(size):
                node, verticalOrder, level = q.popleft()
                dict_order[verticalOrder].append( (level, node.val) )
                if node.left: 
                    q.append((node.left, verticalOrder - 1, level + 1))
                if node.right:
                    q.append((node.right, verticalOrder + 1, level + 1))
        """
        # below are the same to get dict_order
        res = [(vo, sorted(levelVal, key=lambda x: (x[0], x[1])) ) for vo, levelVal in dict_order.items()]
        res.sort(key = lambda x: x[0])
        # print(res)
        lst_level_value = [lv for verticalOrder, lv in res]
        # print(lst_level_value)
        final_res = []
        for lst_lv in lst_level_value:
            tmp = [v[1] for v in lst_lv]
            final_res.append(tmp)
        return final_res
    
    
