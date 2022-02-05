# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/top-k-frequent-words/

LC215, LC973, LC658, LC347, LC692
"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        c = Counter(words)
        freq = [(freq, key) for key, freq in c.items()]
        
        # refre to LC 347
        def helper(freq, k, res):
            if k <= 0:
                return res
            random.shuffle(freq)
            pivot = freq[0][0]
            left = [d for d in freq if d[0] < pivot]
            equals = [d for d in freq if d[0] == pivot]
            right = [d for d in freq if d[0] > pivot]
            if k <= len(right):
                return helper(right, k, res)
            elif k - len(right) <= len(equals):
                res += [ val for freq, val in right + equals]
                return helper(equals, k - len(right + equals), res)
            else:
                res += [ val for freq, val in right + equals]
                return helper(left, k - len(right + equals), res)
            
        res = helper(freq, k, [])
        res.sort(key = lambda x : (-c[x], x))
        return res[:k]