# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/implement-trie-prefix-tree/

https://labuladong.gitee.io/algo/2/20/47/

LC79, LC212, LC208
"""
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        for char in word:
            if c not in self.tire:
                self.tire[c] = {}
            self.tire = self.tire[c]
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
