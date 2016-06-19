# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-linked-list/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None: # or head.next is None:
            return head
        
        current = head
        pre = None 
        
        while current is not None: 
            temp = current.next 
            current.next = pre
            pre = current
            current = temp 
        head = pre
        
        return head 
        
        """
        if (head == None):
            return None
        if( head.next == None):
            return head
        ret = head
        tmp = head

        head = head.next
        ret.next = None
        while (head!=None):
            tmp = head
            head = head.next
            tmp.next = ret
            ret = tmp
        return ret
        
        """