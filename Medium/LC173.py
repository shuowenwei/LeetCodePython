# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-search-tree-iterator

solution reference link: 

https://leetcode.com/problems/binary-search-tree-iterator/discuss/52642/Two-Python-solutions-stack-and-generator

LC1305, LC173, LC21
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushLeftBranch(root)
        
    def pushLeftBranch(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        outNode = self.stack.pop() 
        self.pushLeftBranch(outNode.right)
        return outNode.val 

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0 

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()