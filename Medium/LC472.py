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
            dp = [False] * (len(s) + 1)
            dp[0] = True
            # dict_word = set(wordDict)
            for i in range(len(s)+1):
                for j in range(i):
                    if dp[j] and s[j:i] in wordDict:
                        dp[i] = -1
            return dp[-1]
        
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