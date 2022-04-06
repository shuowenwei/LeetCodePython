# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/odd-even-linked-list/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        odd, even = head, head.next
        even_head = head.next 
        while odd.next and even.next:
            odd.next = even.next # odd.next != None
            odd = odd.next
            even.next = odd.next # even.next != None
            even = even.next
        odd.next = even_head
        return head
