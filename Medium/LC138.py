# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/copy-list-with-random-pointer/

solution: https://leetcode.com/problems/copy-list-with-random-pointer/solution/

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def __init__(self):
        self.dct_oldNode2newNode = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        if head in self.dct_oldNode2newNode:
            return self.dct_oldNode2newNode[head]
        
        node = Node(head.val)
        self.dct_oldNode2newNode[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node