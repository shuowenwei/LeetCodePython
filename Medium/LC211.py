# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-and-search-word-data-structure-design

https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/774530/Python-Trie-solution-with-dfs-explained

LC208, LC1804, LC648, LC211
"""
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
    
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """        
        def dfs(word, node, i):
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                for child in node.children:
                    if dfs(word, node.children[child], i+1):
                        return True
            if word[i] in node.children:
                return dfs(word, node.children[word[i]], i+1)
            return False
        return dfs(word, self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)