# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-product-of-word-lengths/

solution references: https://discuss.leetcode.com/topic/32692/a-two-line-python-solution-176-ms/4

"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        """
        d = {} 
        for w in words: 
            key = sum(1<<(ord(c) - ord('a')) for c in set(w))
            if key not in d:
                d[key] =len(w) 
            else:
                d[key] = max(d[key],len(w))
                
        res = 0
        for k1,v1 in d.items():
            for k2,v2 in d.items():
                if k1&k2 == 0:
                    res = max(res,v1*v2)
        return res 
        """

        # shortest length 
        #d = dict(sorted((sum(1 << (ord(c) - 97) for c in set(w)), len(w)) for w in words))
        #return max([d[k] * d[K] for k in d for K in d if not k & K] or [0])
        
        # medium length
        #d = {sum(1 << (ord(c) - 97) for c in set(w)): len(w) for w in sorted(words, key=len)}
        #return max([d[k] * d[K] for k in d for K in d if not k & K] or [0])
        
        # faster 
        d = {sum(1 << (ord(c) - 97) for c in set(w)): len(w) for w in sorted(words, key=len)}.items()
        return max([v * V for k, v in d for K, V in d if not k & K] or [0])

        # fasterst??? 
        return max([v * V for (k, v), (K, V) in itertools.combinations(dict(sorted((sum(1 << (ord(c) - 97) for c in set(w)), len(w)) for w in words)).items(), 2) if not K & k] or [0])
                
