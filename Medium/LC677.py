# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/map-sum-pairs/

https://labuladong.gitee.io/algo/2/20/47/

https://leetcode.com/problems/map-sum-pairs/discuss/107508/Python-Efficient-O(k)-Insert-and-Sum-using-Trie

LC79, LC212, LC208
LC208, LC1804, LC648, LC211, LC677
"""
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.sum = 0
        
class MapSum(object):

    def __init__(self):
        self.root = TrieNode()
        self.key2val = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = val - self.key2val.get(key, 0)
        self.key2val[key] = val

        current = self.root
        current.sum += delta
        for letter in key:
            current = current.children[letter]
            current.sum += delta
    
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return 0
        return current.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
