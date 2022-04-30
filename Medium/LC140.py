# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/word-break-ii/

https://leetcode.com/problems/concatenated-words/discuss/836924/Python-Template-Word-Break-I-Word-Break-II-Concatenated-Words

LC139, LC140, LC472
- backtrack
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        dict_word = set(wordDict)
        def backtracking(s, dict_word, tmp, start):
            # print(index, tmp)
            if start == len(s):
                res.append(' '.join(tmp))
                return
            for i in range(start, len(s) + 1): # this must be len(s)+1 since s[i:j] not including j 
                # print('i: ', i)
                if s[start:i] in wordDict:
                    tmp.append(s[start:i])
                    # print(tmp, index, i)
                    backtracking(s, dict_word, tmp, i)
                    tmp.pop()
                    
        backtracking(s, dict_word, [], 0)
        return res
    