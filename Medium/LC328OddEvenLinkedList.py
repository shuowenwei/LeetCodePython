# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/odd-even-linked-list/

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head 
        even = head
        odd = head.next
        odd_head = head.next 
        while even.next and odd.next:
            even.next = odd.next 
            even = even.next 
            odd.next = even.next
            odd = odd.next
        even.next = odd_head
        return head 
