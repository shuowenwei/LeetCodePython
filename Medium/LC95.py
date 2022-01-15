# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/unique-binary-search-trees-ii/

labuladong: https://labuladong.gitee.io/algo/2/18/26/

LC95, LC96

solution: https://leetcode.com/problems/unique-binary-search-trees-ii/solution/

LC95, LC96, LC1373
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
        # solution 1: 
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
        """
        # solution 2: 
        memo = [[ [] for i in range(n+1)] for j in range(n+1)]
        def construct(low, high):
            res = []
            if low > high:
                res.append(None)
                return res
            if len(memo[low][high]) != 0:
                return memo[low][high]
            for i in range(low, high+1): 
                leftTrees = construct(low, i-1)
                rightTrees = construct(i+1, high)
                for l in leftTrees:
                    for r in rightTrees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            memo[low][high] = res
            return res
        return construct(1, n)