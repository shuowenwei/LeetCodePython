# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/search-suggestions-system/

https://leetcode.com/problems/search-suggestions-system/discuss/505444/Python-Intuitive-trie-solution-with-detailed-explanation

LC208, LC1268
Trie
"""
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestions = []
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
            if len(curNode.suggestions) < 3:
                curNode.suggestions.append(word)
        curNode.is_word = True
        
    def find(self, searchWord):
        res = []
        curNode = self.root
        for char in searchWord:
            curNode = curNode.children.get(char, None)
            if curNode is None:
                res.append([])
                break
            else:
                res.append(curNode.suggestions[::])
        for j in range(len(searchWord) - len(res)):
            res.append([])
        return res 

    
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = Trie()
        products.sort()
        for prod in products:
            trie.insert(prod)
            
        return trie.find(searchWord)
