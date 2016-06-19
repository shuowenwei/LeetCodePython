# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/implement-queue-using-stacks/

"""
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack = []
        self.outStack = [] 

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x) 

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        self.outStack.pop() 
        

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]
        
    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack) 
        
    def move(self):
        """
        rtype: nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        
        
