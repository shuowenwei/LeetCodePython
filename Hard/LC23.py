# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/merge-k-sorted-lists/

labuladong: https://labuladong.gitee.io/algo/1/6/

LC21, LC23, LC141, LC142, LC876, LC160, LC19


one solution: https://leetcode.com/problems/merge-k-sorted-lists/discuss/908846/Python-3-commented-O(n-log(k))-faster-than-90.64

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        # the new_head.next is to be returned 
        new_head = ListNode(0)
        cur = new_head
        # initialize heap
        import heapq 
        hq = [(ln.val, i) for i, ln in enumerate(lists) if ln is not None]
        heapq.heapify(hq)
        # find the smallest val among the k listnodes
        while hq:
            min_val, ln_index = heapq.heappop(hq)
            cur.next = ListNode(min_val)
            cur = cur.next 
            # the pointer of the linked list has the min val, must move to the next and push into the heap
            lists[ln_index] = lists[ln_index].next
            if lists[ln_index] is not None: 
                heapq.heappush(hq, (lists[ln_index].val, ln_index) )

        return new_head.next