# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

https://jimmy-shen.medium.com/leetcode-426-convert-binary-search-tree-to-sorted-doubly-linked-list-5f66b3a143a8

must do it in-place
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        if root is None:
            return None
        dummy = Node(-1)
        self.prev = dummy
        
        def traverse_inorder(node):
            if node is None:
                return None 
            traverse_inorder(node.left)
            # inorder operations happen here: 
            self.prev.right = node
            node.left = self.prev
            self.prev = node
            traverse_inorder(node.right)
            
        traverse_inorder(root)
        # // connect head and tail
        self.prev.right = dummy.right
        dummy.right.left = self.prev
        
        return dummy.right
    
        # solution 2: Space: O(n)
        res = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node)
            inorder(node.right)
        inorder(root)
        for i in range(len(res)-1):
            res[i].right = res[i+1]
            res[i+1].left = res[i]
        res[-1].right = res[0]
        res[0].left = res[-1]
        return res[0]
