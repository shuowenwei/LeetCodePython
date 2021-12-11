# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-two-sorted-lists/

labuladong: https://labuladong.gitee.io/algo/1/6/

LC21, LC23, LC141, LC142, LC876, LC160, LC19

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p1 = l1
        p2 = l2
        newHead = ListNode(0)
        res = newHead
        while p1 and p2:
            if p1.val < p2.val:
                newHead.next = p1 
                newHead = newHead.next
                p1 = p1.next 
            else:
                newHead.next = p2
                newHead = newHead.next
                p2 = p2.next 
            
        if p1 and not p2:
            newHead.next = p1
        if p2 and not p1: 
            newHead.next = p2
        return res.next
