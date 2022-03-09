# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-string-chain/

https://leetcode.com/problems/longest-string-chain/discuss/1013746/Python3-dp

"""
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPredecessor(wordA, wordB):
            for i in range(len(wordB)):
                if wordB[:i] + wordB[i+1:] == wordA:
                    return True
            return False
        
        import collections
        dict_length = collections.defaultdict(list)
        words.sort(key = lambda x: len(x))
        for w in words:
            dict_length[len(w)] .append(w)
                
        final_res = 0 
        dp_table = {}
        for w in words:
            dp_table[w] = 1
            if len(w)-1 in dict_length:
                for pre_word in dict_length[len(w)-1]:
                    if isPredecessor(pre_word, w):
                        dp_table[w] = max(dp_table[w], 1 + dp_table[pre_word])
            final_res = max(final_res, dp_table[w])
        # print(dp_table)
        return final_res