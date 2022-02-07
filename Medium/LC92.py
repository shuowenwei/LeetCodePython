# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-linked-list-ii/

LC92, LC25, LC234
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
        def reverseWholeLinkedList(head, till = None):
            pre = None 
            cur = head 
            # nxt = head 
            while cur is not till:
                nxt = cur.next
                cur.next = pre
                pre = cur 
                cur = nxt 
            return pre, cur
            # pre is the new head 
            # cur is till
        # 1 -> 2 -> 3 -> 4 -> 5 -> None, left = 2, right = 5 
        dummyHead = ListNode(-1)
        dummyHead.next = head 
        first_part = dummyHead
        for i in range(left-1):
            first_part = first_part.next
        
        second_part = head
        for j in range(right):
            second_part = second_part.next
        # first_part = 1
        # second_part = 5 
        # reverse [left-right] --> [2, 4]
        pre, cur = reverseWholeLinkedList(first_part.next, second_part) # (2, 5)
        # pre = 4, the new head of the reversed part
        # cur = 5, which is the "till"
        # first_part = 1 still and first_part.next still points to 2
        first_part.next.next = cur # point the next of the reversed part to the second part
        first_part.next = pre # first_part.next points to the new head of the reversed part
        return dummyHead.next
    
        # notes from LC206
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