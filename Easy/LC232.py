# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/implement-queue-using-stacks/

https://labuladong.gitee.io/algo/2/20/51/

LC232, LC225

"""
class MyQueue(object):
    
    def __init__(self):
        self.inStack = []
        self.outStack = []
        # self.top = 

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inStack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        _ = self.peek()
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.outStack) == 0:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)
        
        
