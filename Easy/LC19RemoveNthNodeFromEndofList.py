# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """ not really needed 
        if head.next is None and n==1:
            return None
        """
        p1 = p2 = head
        i = 0 
        while i < n:
            p2 = p2.next 
            i += 1
        if p2 is None:
            return head.next 
        while p2 is not None and p2.next is not None:
            p1 = p1.next 
            p2 = p2.next
        if p1.next is not None:
            p1.next = p1.next.next 
            return head 
        
