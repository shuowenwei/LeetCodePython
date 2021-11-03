# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/unique-binary-search-trees-ii/

solution: https://leetcode.com/problems/unique-binary-search-trees-ii/solution/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        def gen_trees(start, end):
            if start > end:
                return None
            all_trees = [] 
            for i in range(start, end + 1):
                #pick i as the root 
                leftTrees = gen_trees(start, i - 1) 
                rightTrees = gen_trees(i+1, end)
                
                for l in leftTrees or [None]:
                    for r in rightTrees or [None]:
                        curTree = TreeNode(i)
                        curTree.left = l 
                        curTree.right = r 
                        all_trees.append(curTree)
            
            return all_trees 
        
        return gen_trees(1, n) if n else []
        