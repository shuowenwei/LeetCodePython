# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-tree-right-side-view/

solution: https://leetcode.com/problems/binary-tree-right-side-view/solution/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        #DFS method 
        right_val_at_depth = {}
        max_depth = -1 
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            
            if node is not None: 
                max_depth = max(max_depth, depth)
                # at each depth level, only insert one val/first val (the most right one) at that depth 
                if depth not in right_val_at_depth:
                    right_val_at_depth[depth] = node.val 
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth +1 )) # sicne using stack, thus "right" later 
        return [right_val_at_depth[depth] for depth in range(max_depth+1)] 
        """
        #BFS
        right_val_at_depth = {}
        max_depth = -1 
        
        queue = collections.deque([(root, 0)]) # first in
        while queue:
            node, depth = queue.popleft() #first out 
            if node is not None: 
                max_depth = max(max_depth, depth)
                
                if depth not in right_val_at_depth:
                    right_val_at_depth[depth] = node.val 
                queue.append((node.right, depth+1))
                queue.append((node.left, depth+1))
                
        return [right_val_at_depth[depth] for depth in range(max_depth+1)] 
        """
