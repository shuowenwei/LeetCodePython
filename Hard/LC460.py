# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/lfu-cache/
https://mp.weixin.qq.com/s/oXv03m1J8TwtHwMJEZ1ApQ
https://leetcode.com/problems/lfu-cache/discuss/800188/Python-O(1)-using-DLL-and-Dictionary

# LC146, LC460
"""
class ListNode(object):
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.freq = 1
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
        :type x: node
        """
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

class LFUCache(object): 
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import collections
        self.key2Node = dict() # hashmap key:int --> node: ListNode
        self.freq2Keys = collections.defaultdict(DoubleList) # hashmap freq:int --> keys:DoubleList[ListNode]
        self.cap = capacity
        self.minFreq = 0

    def increaseFreq(self, key):
        node = self.key2node[key]
        old_freq = node.freq
        self.freq2Keys[old_freq].remove(node)
        node.freq += 1 
        # print('oldFreq',oldFreq, 'newFreq',newFreq)
        self.freq2Keys[node.freq].addLast(node)
        if old_freq == self.minFreq and self.freq2Keys[old_freq].size == 0:
            self.minFreq += 1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2Node:
            return -1 
        self.increaseFreq(key)
        # print('GET:', 'self.freq2Keys[1] size', self.freq2Keys[1].getSize(), \
        #       'self.freq2Keys[2] size', self.freq2Keys[2].getSize(), 'minFreq:', self.minFreq)
        return self.key2Node[key].val
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap <= 0:
            return
        if key in self.key2Node:
            self.key2Node[key].val = value 
            self.increaseFreq(key)
            return # must return here if key exists !!!
        
        if self.cap == len(self.key2Node):
            self.removeMinFreqKey()
            
        newNode = ListNode(key, value)
        self.key2Node[key] = newNode
        self.minFreq = 1
        self.freq2Keys[1].addLast(newNode)
        # print('PUT', 'self.freq2Keys[1] size', self.freq2Keys[1].getSize(), \
        #       'self.freq2Keys[2] size', self.freq2Keys[2].getSize(), 'minFreq:', self.minFreq)
        
    def removeMinFreqKey(self):
        keyList = self.freq2Keys[self.minFreq]
        deletedKey = keyList.removeFirst()
        # print('removeMinFreqKey is called, keyList size:', keyList.getSize() )
        # print('REMOVE:', 'self.freq2Keys[1] size', self.freq2Keys[1].getSize(), \
        #       'self.freq2Keys[2] size', self.freq2Keys[2].getSize(), 'minFreq:', self.minFreq)
        if keyList.getSize() == 0: 
            del self.freq2Keys[self.minFreq] 
            # // 问：这里需要更新 minFreq 的值吗？ - No
            # 实际上没办法快速计算minFreq，只能线性遍历FK表或者KF表来计算，这样肯定不能保证 O(1) 的时间复杂度。
            # 但是，其实这里没必要更新minFreq变量，因为你想想removeMinFreqKey这个函数是在什么时候调用？在put方法中插入新key时可能调用。
            # 而你回头看put的代码，插入新key时一定会把minFreq更新成 1，所以说即便这里minFreq变了，我们也不需要管它。
        # print('keys to be deleted: ', deletedKey.key, 'among', self.key2Node)
        del self.key2Node[deletedKey.key]
