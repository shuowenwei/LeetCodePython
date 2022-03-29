# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sort-list/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)
        
        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        dummy = p = ListNode(0)
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next

        # my long and ugly heap solutiono 
        from heapq import heappush, heappop
        hp = []
        while head:
            heappush(hp, (head.val, head))
            head = head.next
        dummy = ListNode(-1)
        newHead = dummy
        while hp:
            _, cur_node = heappop(hp)
            newHead.next = cur_node
            newHead = newHead.next
        newHead.next = None # otherwise it may found a cycle 
        return dummy.next
