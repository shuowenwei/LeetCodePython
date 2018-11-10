# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/binary-search-tree-iterator

solution reference link: 

https://leetcode.com/problems/binary-search-tree-iterator/discuss/52642/Two-Python-solutions-stack-and-generator

"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0 

    def next(self):
        """
        :rtype: int
        """
        outnode = self.stack.pop() 
        x = outnode.right 
        while x is not None:
            self.stack.append(x)
            x = x.left 
        return outnode.val 
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())