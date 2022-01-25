# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-break/

https://leetcode.com/problems/concatenated-words/discuss/836924/Python-Template-Word-Break-I-Word-Break-II-Concatenated-Words

LC139, LC140, LC472
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
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
                        dp_table[s] = True 
                        return True
            dp_table[s] = False
            return False
        return dp(s, dict_word)
