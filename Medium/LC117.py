# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return root 
        queue = [root]
        while len(queue) > 0:
            queue_size = len(queue)
            for i in range(queue_size):
                cur = queue.pop(0)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                if i < queue_size-1:
                        cur.next = queue[0]
        return root