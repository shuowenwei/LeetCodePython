# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/palindrome-linked-list/

https://labuladong.gitee.io/algo/2/17/19/

LC92, LC25, LC234
LC234, LC5, LC1312, LC516
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # solution from https://leetcode.com/discuss/105410/beats-python-solution-using-stack-complexity-space-complexity 
        # Python solution using a stack with O(N) time complexity and O(N/2) space complexity 
        if not head or not head.next: 
            return True 
        fast = slow = current = head 
        # get the midpoint (slow) 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        
        # 如果fast指针没有指向null，说明链表长度为奇数，slow还要再前进一步：
        if fast is not None:  
            slow = slow.next

        # push the 2nd hal into the stack 
        stack = [] 
        while slow:
            stack.append(slow.val) 
            slow = slow.next
        
        # comparison
        while stack: 
            if stack.pop() != current.val:
                return False
            current = current.next 
        return True 
        
        """
        # solution 2: post order taverse
        left = head 
        pList = [left]
        def traverse(right):
            if right is None:
                return True
            res = traverse(right.next)
            res = res and (pList[0].val == right.val)
            pList[0] = pList[0].next 
            return res
        return traverse(head)
        
        # solution 3: minmimal memory
        def reverseWholeLinkedList(head, till = None):
            pre = None 
            cur = head 
            nxt = head 
            while cur is not till:
                nxt = cur.next
                cur.next = pre
                pre = cur 
                cur = nxt 
            return pre, cur
            # pre is the new head 
            # cur is till
        
        fast = slow = head 
        # get the midpoint (slow) 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        # 如果fast指针没有指向null，说明链表长度为奇数，slow还要再前进一步：
        if fast is not None:  
            slow = slow.next
        
        left = head
        right, _ = reverseWholeLinkedList(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        """
        