# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/concatenated-words/

https://leetcode.com/problems/concatenated-words/discuss/836924/Python-Template-Word-Break-I-Word-Break-II-Concatenated-Words

LC139, LC140, LC472
- backtrack
"""
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # code form LC139
        def wordBreak(s, wordDict):
            dp_table = {}
            dict_word = set(wordDict)
            def dp(s, dict_word):
                if s == '' or s in dict_word:
                    dp_table[s] = True
                    return True
                if s in dp_table:
                    return dp_table[s]
                res = False
                for i in range(len(s)):
                    if s[:i] in wordDict:
                        dp_table[s[:i]] = True
                        if dp(s[i:], wordDict) is True:
                            res = True 
                            break
                dp_table[s] = res
                return res
            return dp(s, dict_word)
        
        res = []
        if len(words) < 2:
            return res
        words.sort(key = lambda x:len(x)) #print(words)
        shorter_words = set()
        for w in words:
            if wordBreak(w, shorter_words):
                res.append(w)
            shorter_words.add(w)
        return res 