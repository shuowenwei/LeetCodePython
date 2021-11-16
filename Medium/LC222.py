# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-complete-tree-nodes/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: 
            return 0 
        
        leftHeight = 0 
        leftPointer = root
        while leftPointer:
            leftHeight+=1 
            leftPointer = leftPointer.left
            
        rightHeight = 0 
        rightPointer = root 
        while rightPointer:
            rightHeight+=1 
            rightPointer = rightPointer.right
            
        if leftHeight == rightHeight:
            return 2**leftHeight - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# Prove: ( log(n) ) ^ k <?? n

# log( ( log(n) ) ^ k  ) <? log(n)
# k * log(log(n)) <? log(n)

# since log(x) < x, hence log(log(n)) < log(n)
# if k is finite, then k * log(log(n)) <? log(n)

