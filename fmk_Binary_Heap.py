# 二叉堆（Binary Heap）其主要操作就两个，sink（下沉）和 swim（上浮），用以维护二叉堆的性质。
# 其主要应用有两个，首先是一种排序方法「堆排序」，第二是一种很有用的数据结构「优先级队列」。

# 二叉堆在逻辑上其实是一种特殊的二叉树（完全二叉树），只不过存储在数组里。一般的链表二叉树，我们操作节点的指针，而在数组里，我们把数组索引作为指针:
# // 父节点的索引


class MaxPQ(object):
    def __init__(self, capacity):
        #  // 索引 0 不用，所以多分配一个空间
        self.pq = [0] * (capacity+1)
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

    def delMax(self, e):
        pass 

    def swim(self, e):
        pass 

    def sink(self, e):
        pass 

    def exchange(self, i, j):
        tmp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = tmp

    def less(self, i, j):
        return i < j