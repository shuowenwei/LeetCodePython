# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/my-calendar-i/


MJ: https://www.1point3acres.com/bbs/thread-841619-1-1.html

LC729, LC731, LC732
"""
class MyCalendar(object):
    
    def __init__(self):
        self.clnd = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # my long and ugly solution: 
        if len(self.clnd) == 0:
            self.clnd.append([start, end])
            return True
        if len(self.clnd) == 1:
            cur_intl = self.clnd[0]
            if end <= cur_intl[0]:
                self.clnd = [[start, end]] + self.clnd
                return True
            elif start >= cur_intl[1]:
                self.clnd = self.clnd + [[start, end]]
                return True 
            else:
                return False 
        
        flag = False
        insert_index = 0 # insert after this index
        for i in range(len(self.clnd)-1):
            cur_intl = self.clnd[i]
            nxt_intvl = self.clnd[i+1]
            # insert 1: 
            if i == 0 and end <= cur_intl[0]:
                insert_index = i
                flag = True
            elif start >= cur_intl[1] and end <= nxt_intvl[0]:
                insert_index = i+1
                flag = True
            elif i == len(self.clnd)-2 and start >= nxt_intvl[1]:
                insert_index = i+2
                flag = True
            else:
                pass 
        if flag:
            self.clnd = self.clnd[:insert_index] + [[start, end]] + self.clnd[insert_index:]
            # print(self.clnd)
        return flag
    
        # neat solution: 
        for s, e in self.clnd:
            if start < e and end > s:
                return False
        self.clnd.append((start, end))
        return True

# solution 2: Binary search tree:
"""
class TreeNode():
    	def __init__(self, start, end):
		self.s = start
		self.e = end
		self.left = None
		self.right = None

class MyCalendar(object):
    def __init__(self):
        self.root = None
        
    def insert(self, s, e, node):
        if s >= node.e:
            if node.right:
                return self.insert(s, e, node.right)
            else:
                node.right = TreeNode(s, e)
                return True
        elif e <= node.s:
            if node.left:
                return self.insert(s, e, node.left)
            else:
                node.left = TreeNode(s, e)
                return True
        else:
            return False
        
    def book(self, start, end):
        # :type start: int
        # :type end: int
        # :rtype: bool
        if not self.root:
			self.root = TreeNode(start, end)
			return True
        return self.insert(start, end, self.root)
"""
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)