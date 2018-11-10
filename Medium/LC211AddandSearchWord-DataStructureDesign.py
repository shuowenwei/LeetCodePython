# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-and-search-word-data-structure-design
solution: 
https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59549/Python-168ms-beat-100-solution

"""
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = {}
        #self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word is not None and len(word) not in self.word_dict:
            self.word_dict[len(word)] = [word]
        else:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) not in self.word_dict:
            return False
        
        if '.' not in word:
            return word in self.word_dict[len(word)]
            
        for e in self.word_dict[len(word)]:
            flag = True
            for i in range(len(word)):
                if e[i] != word[i] and word[i] != '.' :
                    flag = False
                    break
            if flag:
                return True 
        return False 

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

