# https://labuladong.gitee.io/algo/2/20/44/
# https://mp.weixin.qq.com/s/oXv03m1J8TwtHwMJEZ1ApQ
# LFU - Least Frequently Used

# 而 LFU 算法相当于是把数据按照访问频次进行排序，这个需求恐怕没有那么简单，
# 而且还有一种情况，如果多个数据拥有相同的访问频次，我们就得删除最早插入的那个数据。也就是说 LFU 算法是淘汰访问频次最低的数据，
# 如果访问频次最低的数据有多条，需要淘汰最旧的数据。

# 1、使用一个 HashMap 存储 key 到 val 的映射，就可以快速计算 get(key)。
# 2、使用一个 HashMap 存储 key 到 freq 的映射，就可以快速操作 key 对应的 freq。
# 3、这个需求应该是 LFU 算法的核心，所以我们分开说。
# 3.1、首先，肯定是需要 freq 到 key 的映射，用来找到 freq 最小的 key。
# 3.2、将 freq 最小的 key 删除，那你就得快速得到当前所有 key 最小的 freq 是多少。想要时间复杂度 O(1) 的话，
# 肯定不能遍历一遍去找，那就用一个变量 minFreq 来记录当前最小的 freq 吧。
# 3.3、可能有多个 key 拥有相同的 freq，所以 freq 对 key 是一对多的关系，即一个 freq 对应一个 key 的列表。
# 3.4、希望 freq 对应的 key 的列表是存在时序的，便于快速查找并删除最旧的 key。
# 3.5、希望能够快速删除 key 列表中的任何一个 key，因为如果频次为 freq 的某个 key 被访问，那么它的频次就会变成 freq+1，
# 就应该从 freq 对应的 key 列表中删除，加到 freq+1 对应的 key 的列表中。

# LC146, LC460

class ListNode(object):
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.freq = 1
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
        self.key2Val = dict() # hashmap key:int --> node: ListNode
        self.freq2Keys = collections.defaultdict(DoubleList) # hashmap freq:int --> keys:DoubleList[ListNode]
        self.cap = capacity
        self.minFreq = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2Val:
            return -1 
        self.increaseFreq(key)
        return self.key2Val[key].val
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key2Val:
            self.key2Val[key] = value 
            self.increaseFreq(key, val)
            return # must return here if key exists !!!
        
        if self.cap <= len(self.key2Val):
            self.removeMinFreqKey()
            
        newNode = ListNode(key, value)
        self.key2Val[key] = newNode
        self.minFreq = 1
        if self.freq2Keys.get(1) :
            self.freq2Keys[1].addLast(newNode)
        else: 
            self.freq2Keys[1] = DoubleList(head=Node(0,0), tail=newNode)

    def increaseFreq(self, key):
        oldFreq = self.key2Freq[key]
        self.key2Freq[key].freq += 1
        newFreq = self.key2Freq[key].freq
        self.freq2Keys[oldFreq].remove(key)
        self.freq2Keys[newFreq].addLast(key)
        if oldFreq == self.minFreq and self.freq2Keys[oldFreq].getSize() == 0:
            self.minFreq += 1 
        
    def removeMinFreqKey(self, key):
        keyList = self.freq2Keys[self.minFreq]
        deletedKey = keyList.removeFirst()
        if deletedKey.getSize() == 0: 
            del self.freq2Keys[self.minFreq] 
            # // 问：这里需要更新 minFreq 的值吗？ - No
            # 实际上没办法快速计算minFreq，只能线性遍历FK表或者KF表来计算，这样肯定不能保证 O(1) 的时间复杂度。
            # 但是，其实这里没必要更新minFreq变量，因为你想想removeMinFreqKey这个函数是在什么时候调用？在put方法中插入新key时可能调用。
            # 而你回头看put的代码，插入新key时一定会把minFreq更新成 1，所以说即便这里minFreq变了，我们也不需要管它。
        del self.key2Val[deletedKey]

    # def makeRecently(self, key):
    #     node = self.map[key]
    #     self.cache.remove(node) # // 先从链表中删除这个节点
    #     self.cache.addLast(node) # // 重新插到队尾
        
    # def addRecently(self, key, val):
    #     newNode = Node(key, val)
    #     self.cache.addLast(newNode) # // 链表尾部就是最近使用的元素
    #     self.map[key] = newNode # // 别忘了在 map 中添加 key 的映射
        
    # def deleteKey(self, key): 
    #     node = self.map[key]
    #     self.cache.remove(node) # // 从链表中删除
    #     self.map.pop(key) # // 从 map 中删除

    # def removeLeastRecently(self):
    #     deletedNode = self.cache.removeFirst()
    #     deletedKey = deletedNode.key
    #     # print('key to remove:', deletedKey, self.map.get(deletedKey))
    #     if self.map.get(deletedKey) is not None:
    #         del self.map[deletedKey]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)