# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

solution reference: https://discuss.leetcode.com/topic/54877/python-reservoir-sampling-solution-when-the-length-of-linked-list-changes-dynamically/2

geek4geek link: http://www.geeksforgeeks.org/reservoir-sampling/

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head 

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0,index) is 0:
                result = node
            node=node.next
            index += 1
        return result.val 


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()