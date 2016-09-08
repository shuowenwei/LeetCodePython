# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/linked-list-random-node/

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint, random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0 
        while head:
            self.length += 1 
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        choice = randint(0, self.length-1)
        i = 0
        p = self.head 
        while i < choice:
            p = p.next
            i += 1
        return p.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()