# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/sort-list/

https://leetcode.com/problems/sort-list/discuss/892759/Python-O(n-log-n-log-n)-merge-sort-explained

LC876, LC148
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
        # solution 1: merge sort 
        if not head or not head.next: return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def getMid(self, head): # refer to LC876
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self, head1, head2):
        dummy = tail = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next, tail, head1 = head1, head1, head1.next
            else:
                tail.next, tail, head2 = head2, head2, head2.next
        tail.next = head1 or head2
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
