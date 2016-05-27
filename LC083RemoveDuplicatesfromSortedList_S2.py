# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
            
        current = head 
        while current is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next 
            
        return head 