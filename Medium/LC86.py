# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/linked-list-cycle-ii/

https://labuladong.github.io/algo/2/19/18/

LC21, LC23, LC141, LC142, LC876, LC160, LC19, LC86
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummySmall = ListNode(-1)
        dummyLarge = ListNode(-1)
        pSmall = dummySmall
        pLarge = dummyLarge
        p = head
        while p:
            if p.val < x:
                pSmall.next = p
                pSmall = pSmall.next
            else:
                pLarge.next = p
                pLarge = pLarge.next
            # // 断开原链表中的每个节点的 next 指针
            temp = p.next
            p.next = None
            p = temp 
            
        pSmall.next = dummyLarge.next
        
        return dummySmall.next