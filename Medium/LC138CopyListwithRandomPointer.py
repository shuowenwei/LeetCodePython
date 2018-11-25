# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/copy-list-with-random-pointer/

solution: https://leetcode.com/problems/copy-list-with-random-pointer/solution/

"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def __init__(self):
        self.visitedHash = {} 
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None 
        if head in self.visitedHash:
            return self.visitedHash[head]
        node = RandomListNode(head.label)
        self.visitedHash[head] = node 
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node 