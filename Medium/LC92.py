# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-linked-list-ii/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummyHead = ListNode(-1)
        dummyHead.next = head 
        first_part = dummyHead
        for i in range(left-1):
            first_part = first_part.next
        
        # reverse [m-n]
        pre = None
        cur = first_part.next 
        for i in range(right-left+1):
            tmp = cur.next 
            cur.next = pre
            pre = cur
            cur = tmp 

        first_part.next.next = cur # first_part.next still points to 2
        first_part.next = pre    
        return dummyHead.next
    
        # # def reverseList(self, head, till=None):
        # pre = None 
        # cur = head
        # nxt = head 
        # while cur is not None: #(cur != till)
        #     nxt = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = nxt
        # return pre