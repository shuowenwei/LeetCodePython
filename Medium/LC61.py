# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/rotate-list/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head 
        n = 1
        while head.next:
            head = head.next
            n += 1
        head.next = dummy.next
        p = dummy.next
        q = dummy.next
        k = k % n
        for i in range(n-k):
            p = p.next
        while q.next != p:
            q = q.next
        q.next = None
        return p 

