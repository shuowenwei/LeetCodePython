# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

LC323, LC130, LC990

"""
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
            x = self.parent[x]
        return x
        
    def count(self):
        return self.cnt

    def connected(self, p, q):
        rootP = self.find(p) 
        rootQ = self.find(q)
        return rootP == rootQ
    
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf = UnionFind(26)
        for eq in equations:
            if eq[1] == '=':
                letterOne = ord(eq[0]) - ord('a')
                letterTwo = ord(eq[3]) - ord('a')
                uf.union(letterOne, letterTwo)
        for eq in equations:
            if eq[1] == '!':
                letterOne = ord(eq[0]) - ord('a')
                letterTwo = ord(eq[3]) - ord('a')
                if uf.connected(letterOne, letterTwo):
                    return False
        return True