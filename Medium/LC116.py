# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

https://labuladong.gitee.io/algo/2/19/23/

LC226, LC114, LC116
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
        # solution 1: recursively via a helper function 
        """
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
        
        # solution 2: recursively without a helper function 
        """
        if root and root.left and root.right: 
            root.left.next = root.right
            if root.next: # 2's right child 5, need to connect to 6, which is 3' left child
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
        """
        
        # solution 3: BFS
        if root is None:
            return root
        q = collections.deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                cur_node = q.popleft()
                if i < size - 1:
                    cur_node.next = q[0]
                # else:
                #     cur_node.next = None
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
        return root
    
