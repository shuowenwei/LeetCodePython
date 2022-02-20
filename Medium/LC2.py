# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-two-numbers/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        carry = 0 
        while l1 and l2:
            res = (l1.val + l2.val + carry) % 10 
            carry = (l1.val + l2.val + carry) / 10 
            p.next = ListNode(res)
            p = p.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            res = (l1.val + carry) % 10 
            carry = (l1.val + carry) / 10 
            p.next = ListNode(res)
            p = p.next
            l1 = l1.next
            
        while l2:
            res = (l2.val + carry) % 10 
            carry = (l2.val + carry) / 10 
            p.next = ListNode(res)
            p = p.next
            l2 = l2.next
            
        if carry > 0:
            p.next = ListNode(carry)
            
        return dummy.next
