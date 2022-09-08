# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/design-linked-list/

"""
class ListNode(object):
    def __init__(self, val=0):
        self.val = val

class MyLinkedList(object):

    def __init__(self):
        self.NodeArray = []
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index > len(self.NodeArray)-1:
            return -1
        node = self.NodeArray[index]
        return node.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val)
        self.NodeArray = [newNode] + self.NodeArray
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val)
        self.NodeArray.append(newNode)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > len(self.NodeArray):
            return 
        elif index == len(self.NodeArray):
            self.addAtTail(val)
        else:
            newNode = ListNode(val)
            self.NodeArray = self.NodeArray[:index] + [newNode] + self.NodeArray[index:]
            # print(index, val, [n.val for n in self.NodeArray])

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index > len(self.NodeArray)-1:
            return
        elif index == len(self.NodeArray):
            self.NodeArray.pop()
        else:
            self.NodeArray = self.NodeArray[:index] + self.NodeArray[index+1:]
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
