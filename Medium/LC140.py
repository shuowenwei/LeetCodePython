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
        dp_table = {}
        dict_word = set(wordDict)
        def backtracking(s, dict_word, tmp, index):
            # print(index, tmp)
            if index == len(s):
                res.append(' '.join(tmp))
                return
            for i in range(index, len(s) + 1): # this must be len(s)+1 since s[i:j] not including j 
                # print('i: ', i)
                if s[index:i] in wordDict:
                    tmp.append(s[index:i])
                    # print(tmp, index, i)
                    backtracking(s, dict_word, tmp, i)
                    tmp.pop()
                    
        backtracking(s, dict_word, [], 0)
        return res
    