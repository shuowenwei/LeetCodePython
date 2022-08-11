# https://labuladong.gitee.io/algo/2/20/50/

# 二叉堆（Binary Heap）其主要操作就两个，sink（下沉）和 swim（上浮），用以维护二叉堆的性质。
# 其主要应用有两个，首先是一种排序方法「堆排序」，第二是一种很有用的数据结构「优先级队列」。

# 二叉堆在逻辑上其实是一种特殊的二叉树（完全二叉树），只不过存储在数组里。一般的链表二叉树，我们操作节点的指针，而在数组里，我们把数组索引作为指针:
# // 父节点的索引

class MaxPQ(object):
    def __init__(self, capacity):
        #  // 索引 0 不用，所以多分配一个空间
        self.pq = [None] * (capacity+1)
        self.N = 0

    def parent(self, root: int):
        return root / 2

    # // 左孩子的索引
    def left(self, root: int):
        return root * 2

    # // 右孩子的索引
    def right(self, root: int):
        return root * 2 + 1

    def max(self):
        return self.pq[1]

    def delMax(self):
        maxVal = self.pq[1]
        self.exchange(1, self.N)
        self.pq[self.N] = None
        self.N -= 1 
        self.sink(1)
        return maxVal
    
    def insert(self, e):
        self.N += 1 
        self.pq[self.N] = e 
        self.swim(self.N)

    # /* 上浮第 k 个元素，以维护最大堆性质 */
    def swim(self, e):
        while k > 1 and self.less(self.parent(k), k):
        # // 如果第 k 个元素比上层大
        # // 将 k 换上去
            self.exch(parent(k), k)
            k = self.parent(k)

    # /* 下沉第 k 个元素，以维护最大堆性质 */
    def sink(self, k):
        # // 如果沉到堆底，就沉不下去了
        while self.pq[k] <= self.N:
            # // 先假设左边节点较大
            older = self.left(k)
            # // 如果右边节点存在，比一下大小
            if self.right(k) <= self.N and self.less(older, self.right(k)):
                older = self.right(k)
            # // 结点 k 比俩孩子都大，就不必下沉了
            if self.less(older, k):
                break
            # // 否则，不符合最大堆的结构，下沉 k 结点
            self.exch(k, older)
            k = older

    def exchange(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def less(self, i, j):
        return i < j
