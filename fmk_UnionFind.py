# https://labuladong.gitee.io/algo/2/19/37/

# 我们使用森林（若干棵树）来表示图的动态连通性，用数组来具体实现这个森林。
class UnionFind(object):
    def __init__(self, count):
        self.cnt = count
        self.parent = [i for i in range(count)] 
        # for i in range(count):
        #     self.parent[i] = i
        self.size = [1 for i in range(count)]

    def union(self, p, q):
        rootP = self.find(p) 
        rootQ = self.find(q)
        if rootP == rootQ: # already connected, do nothing and return
            return 
        # // 小树接到大树下面，较平衡
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.cnt -= 1
        # find , union , connected 的时间复杂度从O(N)都下降为 O(logN)，即便数据规模上亿，所需时间也非常少
        
    def find(self, x):
        # 可见，调用 find 函数每次向树根遍历的同时，顺手将树高缩短了，最终所有树高都不会超过 3（union 的时候树高可能达到 3）。
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]] # O(1)
        return x
        
    def count(self):
        return self.cnt

    def connected(p, q):
        rootP = self.find(p) 
        rootQ = self.find(q)
        return rootP == rootQ

# 1、用 parent 数组记录每个节点的父节点，相当于指向父节点的指针，所以 parent 数组内实际存储着一个森林（若干棵多叉树）。
# 2、用 size 数组记录着每棵树的重量，目的是让 union 后树依然拥有平衡性，而不会退化成链表，影响操作效率。
# 3、在 find 函数中进行路径压缩，保证任意树的高度保持在常数，使得 union 和 connected API 时间复杂度为 O(1)。

# 因为路径压缩保证了树高为常数（不超过 3），那么树就算不平衡，高度也是常数，基本没什么影响。
# 论时间复杂度的话，确实，不需要重量平衡也是 O(1)。但是如果加上 size 数组辅助，效率还是略微高一些。

uf = UnionFind(10)
print(uf.count())