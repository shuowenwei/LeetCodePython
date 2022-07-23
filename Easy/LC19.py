# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

https://labuladong.github.io/algo/2/19/18/

LC21, LC23, LC141, LC142, LC876, LC160, LC19, LC86
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
        # 返回链表的倒数第 k 个节点
        def findFromEnd(head, k):
            p1, p2 = head, head
            # p1 先走 k 步
            for i in range(k):
                p1 = p1.next
            # p1 和 p2 同时走 n - k 步 (n is the length of listNode head)
            while p1 is not None:
                p1 = p1.next
                p2 = p2.next
            # p2 现在指向第 n - k 个节点
            return p2 
        
        dummy = ListNode(-1)
        dummy.next = head 
        
        # since dummy is extra node added to the front of head
        node2remove = findFromEnd(dummy, n+1) 
        node2remove.next = node2remove.next.next
        
        return dummy.next # do not return head, since it could be removed already 
        """
        # solution 2:
        p1 = p2 = head
        i = 0

        for i in range(n):
            p2 = p2.next  # p2 先走 n 步

        if p2 is None: # head is to be returbed 
            return head.next

        while p2 is not None and p2.next is not None:
            p1 = p1.next 
            p2 = p2.next
            
        if p1.next is not None:
            p1.next = p1.next.next 
            return head 
        """