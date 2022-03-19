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
        if root is None:
            return []
        res = []
        def traverse_dfs(node, row, col):
            if node is None:
                return 
            res.append((node.val, row, col))
            traverse_dfs(node.left, row + 1, col - 1)
            traverse_dfs(node.right, row + 1, col + 1)            
        traverse_dfs(root, 0, 0)
        res.sort(key = lambda x: [x[2], x[1], x[0]])
        
        final_res = []
        cur_col = res[0][2]
        tmp = []
        for val, row, col in res:
            if cur_col == col: 
                tmp.append(val)
            else:
                final_res.append(tmp[:])
                tmp = [val]
                cur_col = col
        if tmp:
            final_res.append(tmp[:])
        return final_res
    
        # longer solution 2
        dct_vo2lstVals = collections.defaultdict(list)
        # solution 1: DFS 
        def traverse(node, vo, level):
            if node is None:
                return 
            dct_vo2lstVals[vo].append((level, node.val))
            traverse(node.left, vo - 1, level + 1)
            traverse(node.right, vo + 1, level + 1)
        traverse(root, 0, 0)
        # solution 2: BFS 
        """
        q = collections.deque()
        level = 0
        vo = 0 
        q.append((root, vo, level))
        while q:
            size = len(q)
            for i in range(size):
                node, vo, level = q.popleft()
                dct_vo2lstVals[vo].append( (level, node.val) )
                if node.left: 
                    q.append((node.left, vo - 1, level + 1))
                if node.right:
                    q.append((node.right, vo + 1, level + 1))
        """
        # below are the same to get dict_order
        res = [[vo, sorted(lst, key=lambda x: (x[0], x[1]) )] for vo, lst in dct_vo2lstVals.items()]
        res.sort(key=lambda x: x[0])
        final_res = []
        for vo, levelVals in res:
            final_res.append([levelVal[1] for levelVal in levelVals])
        return final_res
    
    
