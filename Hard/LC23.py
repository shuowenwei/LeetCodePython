# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-k-sorted-lists/

https://labuladong.github.io/algo/2/19/18/

LC21, LC23, LC141, LC142, LC876, LC160, LC19, LC86
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop 
        hp = []
        # the dummy_head.next is to be returned 
        dummy_head = ListNode(-1)
        cur = dummy_head
        for ln_head in lists:
            if ln_head:
                heappush(hp, (ln_head.val, ln_head)) 

        # find the smallest val among the k listnodes
        while hp:
            _, node = heappop(hp)
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(hp, (node.next.val, node.next))
        return dummy_head.next