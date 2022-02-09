# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/replace-words/

https://labuladong.gitee.io/algo/2/20/47/

LC79, LC212, LC208
LC208, LC1804, LC648, LC211, LC677
"""
class TrieNode(object):
    # Initialize your data structure here.
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
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word 

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
    
    def shortestPrefix(self, query):
        current = self.root
        res = ''
        for i in range(len(query)):
            if current is None:
                return ''
            if current.is_word:
                return res # query[:i] won't work, for single letter input such as 'a'
            letter = query[i]
            current = current.children[letter]
            res += letter
        if current.is_word is False:
            return res
        return res
        
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        res = []
        for sen_word in sentence.split():
            prefix = trie.shortestPrefix(sen_word)
            res.append(prefix)     
        return ' '.join(res)
    
