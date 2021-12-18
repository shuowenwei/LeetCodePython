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
        head.next = tail 
        tail.prev = head 
        self.size = 0
        
    # // 在链表尾部添加节点 x，时间 O(1)
    def addLast(self, x: Node): 
        x.prev = self.tail.prev
        x.next = self.tail
        tail.prev.next = x 
        tail.prev = x 
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
