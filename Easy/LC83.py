# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

https://labuladong.gitee.io/algo/2/21/63/

LC26, LC83, LC27, LC283
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # solution 1: two pointers
        slow, fast = head, head
        while fast is not None:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next

        # // 断开与后面重复元素的连接
        if slow is not None:
            slow.next = None
        return head
    
        # solution 2:
        """
        if head is None or head.next is None:
            return head

        current = head 
        while current is not None and current.next is not None:
            if current.val == current.next.val: 
                current.next = current.next.next
            else:
                current = current.next
        return head 
        """