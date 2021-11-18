# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/reverse-linked-list/

labuladong: https://labuladong.gitee.io/algo/2/17/17/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # solution: recursive, elegant solution: https://labuladong.gitee.io/algo/2/17/17/
        # if head is None:
        #     return None
        # if head.next is None:
        #     return head
        # last = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return last 
        
        # solution 2: one extra pointer
        pre = None 
        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre