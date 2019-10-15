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
        p1 = l1
        p2 = l2 
        res = ListNode(0)
        carry = 0 
        curr = res 
        while p1 and p2:
            node = ListNode((p1.val + p2.val + carry) % 10)  
            carry = (p1.val + p2.val + carry) // 10 
            curr.next = node 
            curr = node
            p1 = p1.next
            p2 = p2.next
        while p1: 
            node = ListNode((p1.val + carry) % 10)
            carry = (p1.val + carry) // 10 
            curr.next = node
            curr = node
            p1 = p1.next
        while p2: 
            node = ListNode((p2.val + carry) % 10)
            carry = (p2.val + carry) // 10 
            curr.next = node
            curr = node
            p2 = p2.next
        if carry > 0: 
            curr.next = ListNode(carry)
        return res.next 

"""
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
"""
