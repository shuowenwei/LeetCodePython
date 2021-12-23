# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/implement-stack-using-queues/

https://labuladong.gitee.io/algo/2/20/51/

LC232, LC225
"""
class MyStack(object):
    
    def __init__(self):
        import collections
        self.q = collections.deque()
        # in this problem, only append() and popleft() are allowed to use 
        # append(): enter queue from the right hand side 
        # popleft(): exit the queue from the left hand side 

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        for i in range(len(self.q)-1): 
            self.q.append(self.q.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()