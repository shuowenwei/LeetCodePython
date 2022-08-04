# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/implement-trie-prefix-tree/

https://labuladong.gitee.io/algo/2/20/47/

https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution

LC79, LC212, LC208, LC1268
LC208, LC1804, LC648, LC211, LC677
Trie
"""
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    
class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curNode = self.root
        for char in word:
            curNode = curNode.children[char]
        curNode.is_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for char in word:
            curNode = curNode.children.get(char, None)
            if curNode is None:
                return False
        return curNode.is_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for char in prefix:
            curNode = curNode.children.get(char, None)
            if curNode is None:
                return False
        return True # curNode.is_word vs search()

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)