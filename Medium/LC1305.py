# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

MG: https://www.1point3acres.com/bbs/thread-841626-1-1.html

LC1305, LC173, LC21
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def traverse(root, res):
            if root is None:
                return 
            traverse(root.left, res)
            res.append(root.val)
            traverse(root.right, res)
        res1, res2 = [], []
        traverse(root1, res1)
        traverse(root2, res2)
        p1, p2 = 0, 0
        res = []
        while p1 < len(res1) and p2 < len(res2):
            if res1[p1] < res2[p2]:
                res.append(res1[p1])
                p1 += 1
            else:
                res.append(res2[p2])
                p2 += 1
        if p1 < len(res1):
            res += res1[p1:]
        if p2 < len(res2):
            res += res2[p2:]
        return res

# solution 2: use iterator, refer to LC173
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
        
    def pushLeftBranch(self, ln):
        while ln is not None:
            self.stack.append(ln)
            ln = ln.left
            
    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1].val 
    
    def next(self):
        """
        :rtype: int
        """
        outnode = self.stack.pop() 
        self.pushLeftBranch(outnode.right)
        return outnode.val 

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0 
    
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res = []
        iter1 = BSTIterator(root1)
        iter2 = BSTIterator(root2)
        # print(iter1, iter2, iter1==iter2)
        while iter1.hasNext() and iter2.hasNext():
            if iter1.peek() > iter2.peek():
                res.append(iter2.next())
            else:
                res.append(iter1.next())
        while iter1.hasNext():
            res.append(iter1.next())
        while iter2.hasNext():
            res.append(iter2.next())
        return res 