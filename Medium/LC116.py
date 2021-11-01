# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

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
        """
        # solution 1: recursively via a helper function 
        if root is None:
            return root 
        def connectLeft2Right(left, right):
            if left is None or right is None:
                return None
            left.next = right
            connectLeft2Right(left.left, left.right)
            connectLeft2Right(right.left, right.right)
            connectLeft2Right(left.right, right.left)
        connectLeft2Right(root.left, root.right)
        return root
        """
        """
        # solution 2: recursively without a helper function 
        if root and root.left and root.right: 
            root.left.next = root.right
            if root.next: # 5 is 2's right child, 6 is 3' left child
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
        """
        # solution 3: BFS
        if root is None:
            return root 
        queue = [root]
        while len(queue) > 0:
            queue_size = len(queue)
            for i in range(queue_size):
                cur = queue.pop(0)
                if cur.left is not None and cur.right is not None:
                    queue.append(cur.left)
                    queue.append(cur.right)
                if i < queue_size-1:
                        cur.next = queue[0]
        return root
