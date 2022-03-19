# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/copy-list-with-random-pointer/

https://leetcode.com/problems/copy-list-with-random-pointer/discuss/258935/Detailed-Explanation-with-Pictures-C%2B%2BJavaScript

"""

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def __init__(self):
        self.dct_oldNode2newNode = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        
        # this is for when head.random is passed in 
        if head in self.dct_oldNode2newNode:
            return self.dct_oldNode2newNode[head]
        
        # create a new node, with old node's val
        newNode = Node(head.val)
        self.dct_oldNode2newNode[head] = newNode

        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)
        
        return newNode
    
    
        # solution 2: do it in while loop 
        if head is None:
            return None
        oldHead = head
        newHead = Node(head.val)
        dummyOldHead = head # dummyOldHead might not be necessary 
        dummyNewHead = newHead
        
        oldNode2newNode = {}
        oldNode2newNode[oldHead] = newHead
        
        while oldHead.next:
            newHead.next = Node(oldHead.next.val)
            oldHead = oldHead.next
            newHead = newHead.next
            oldNode2newNode[oldHead] = newHead
          
        oldHead = dummyOldHead # head
        newHead = dummyNewHead
        while oldHead and newHead:
            if oldHead.random in oldNode2newNode:
                newHead.random = oldNode2newNode[oldHead.random]
            # else:
            #     newHead.random = None
            oldHead = oldHead.next
            newHead = newHead.next
            
        return dummyNewHead
