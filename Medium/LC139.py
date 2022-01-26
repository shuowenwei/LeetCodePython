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
                if s[:i] in dict_word:
                    dp_table[s[:i]] = True
                    if dp(s[i:], dict_word) is True:
                        res = True 
                        break # this makes it faster
            dp_table[s] = res
            return res
        return dp(s, dict_word)

        # solution 2: bottom up
        dp = [False] * (len(s) + 1)
        dp[0] = True
        dict_word = set(wordDict)
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dict_word:
                    dp[i] = -1
        return dp[-1]