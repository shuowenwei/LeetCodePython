# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-two-numbers/

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.num2ListNode(self.ListNode2num(l1) + self.ListNode2num(l2)) 
    
    def num2ListNode(self, num) -> ListNode: 
        head = None
        if num == 0: 
            return ListNode(0)  
        else:
            head = ListNode(num%10) 
        curr = head 
        num = num // 10 
        while num > 0: 
            node = ListNode(num % 10) 
            num = num // 10 
            curr.next = node 
            curr = node 
        return head
        
    def ListNode2num(self, l1: ListNode) -> int: 
        res = 0 
        n = 0 
        if not l1: 
            return res 
        p = l1 
        res = p.val 
        while p.next: 
            n += 1 
            p = p.next 
            res += p.val * 10**n
        return res 
        