# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-nodes-in-k-group/

labuladong: https://labuladong.gitee.io/algo/2/17/18/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def reverseWholeLinkedList(head, till=None):
            pre = None 
            cur = head 
            nxt = head 
            while cur is not till:
                nxt = cur.next
                cur.next = pre
                pre = cur 
                cur = nxt 
            return pre 
        
        if head is None:
            return None 
        a = head
        b = head 
        for i in range(k):
            if b is None:
                return head 
            else:
                b = b.next
        newHead = reverseWholeLinkedList(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead
