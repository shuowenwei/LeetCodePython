# https://labuladong.gitee.io/algo/2/20/43/
# LRU - Least Recently Used

# LRU 缓存算法的核心数据结构就是哈希链表，双向链表和哈希表的结合体。

# 1、如果我们每次默认从链表尾部添加元素，那么显然越靠尾部的元素就是最近使用的，越靠头部的元素就是最久未使用的。
# 2、对于某一个 key，我们可以通过哈希表快速定位到链表中的节点，从而取得对应 val。
# 3、链表显然是支持在任意位置快速插入和删除的，改改指针就行。只不过传统的链表无法按照索引快速访问某一个位置的元素，而这里借助哈希表，
# 可以通过 key 快速映射到任意一个链表节点，然后进行插入和删除。

class Node(object):
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoubleList(object): 
    # // 初始化双向链表的数据
    def __init__(self, head=Node(0,0), tail=Node(0,0) ):
        self.head = head
        self.tail = tail
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
    def remove(self, x: Node):
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

class LRU(object): 
    def __init__(self, capacity):
        self.map = dict() # k: node --> v: val
        self.cap = capacity
        self.cache = DoubleList()
    
    def makeRecently(self, key):
        node = self.map[key]
        self.cache.remove(node) # // 先从链表中删除这个节点
        self.cache.addLast(node) # // 重新插到队尾
        
    def addRecently(self, key, val):
        newNode = Node(key, val)
        self.cache.addLast(newNode) # // 链表尾部就是最近使用的元素
        self.map[key] = newNode # // 别忘了在 map 中添加 key 的映射
        
    def deleteKey(self, key): 
        node = self.map[key]
        self.cache.remove(node) # // 从链表中删除
        self.map.pop(key) # // 从 map 中删除

    def removeLeastRecently(self):
        deletedNode = self.cache.removeFirst()
        deletedKey = deletedNode.key
        self.map.pop(key)
        
    def get(self, key: int): 
        if self.map.get(key) is None:
            return -1 
        self.makeRecently(key)
        return self.map[key].val
    
    def put(key: int, val: int):
        if self.map.get(key): 
            self.deleteKey(key)
            self.addRecently(key, val)
         
        if self.cap == self.cache.getSize():
            self.removeLeastRecently()
            
        self.addRecently(key, val)
