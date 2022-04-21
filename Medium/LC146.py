# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/lru-cache/

solution: https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList
and use orderedDict: https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).  

https://labuladong.gitee.io/algo/2/20/43/

LC146, LC460, LC895
"""
class ListNode(object):
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class DoubleList(object): 
    # // 初始化双向链表的数据
    def __init__(self):
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
        self.size = 0
        
    # // 在链表尾部添加节点 x，时间 O(1)
    def addLast(self, x): 
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x 
        self.tail.prev = x 
        self.size += 1
        
    # // 删除链表中的 x 节点（x 一定存在）
    # // 由于是双链表且给的是目标 Node 节点，时间 O(1)
    def remove(self, x):
        """
        :type x: ListNode
        """
        if x not in (self.head, self.tail):
            x.prev.next = x.next 
            x.next.prev = x.prev 
            self.size -= 1 
        
    # // 删除链表中第一个节点，并返回该节点，时间 O(1)
    def removeFirst(self):
        if self.head.next == self.tail: 
            return None 
        first = self.head.next 
        self.remove(first)
        return first
    
    # // 返回链表长度，时间 O(1)
    def getSize(self):
        return self.size

class LRUCache(object): 
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key2Node = dict() # key:int --> node: ListNode
        self.cap = capacity
        self.cache = DoubleList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.key2Node.get(key) is None:
            return -1 
        # self.makeRecently(key)
        node = self.key2Node[key]
        self.cache.remove(node) # // 先从链表中删除这个节点
        self.cache.addLast(node) # // 重新插到队尾
        return self.key2Node[key].val

    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key2Node:
            node = self.key2Node[key]
            self.cache.remove(node)
            node.val = value 
            self.cache.insertTail(node)
            return # must return here if key exists !!!

        newNode = Node(value, key)
        self.key2Node[key] = newNode
        if self.cache.size == self.cap:
            first = self.cache.removeFirst()  # // 删除最久未使用的元素
            if first is not None:
                del self.key2Node[first.key]
        self.cache.insertTail(newNode) # // 添加为最近使用的元素

    # def makeRecently(self, key):
    #     node = self.key2Node[key]
    #     self.cache.remove(node) # // 先从链表中删除这个节点
    #     self.cache.addLast(node) # // 重新插到队尾
        
    # def addRecently(self, key, val):
    #     newNode = ListNode(key, val)
    #     self.cache.addLast(newNode) # // 链表尾部就是最近使用的元素
    #     self.key2Node[key] = newNode # // 别忘了在 key2Node 中添加 key 的映射
        
    # def deleteKey(self, key): 
    #     node = self.key2Node[key]
    #     self.cache.remove(node) # // 从链表中删除
    #     self.key2Node.pop(key) # // 从 map 中删除

    # def removeLeastRecently(self):
    #     deletedNode = self.cache.removeFirst()
    #     deletedKey = deletedNode.key
    #     # print('key to remove:', deletedKey, self.key2Node.get(deletedKey))
    #     if self.key2Node.get(deletedKey) is not None:
    #         del self.key2Node[deletedKey]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)