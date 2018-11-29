# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/top-k-frequent-words/

"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        wordsCounter = Counter(words)
        res = [(w, v) for w, v in wordsCounter.items()]
        res.sort(key = lambda x: (-x[1], x[0])) 
        #sort by ascending by counts and words from a-z 
        return [w[0] for w in res[:k]]
        
        
                