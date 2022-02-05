# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-product-of-word-lengths/

solution references: https://discuss.leetcode.com/topic/32692/a-two-line-python-solution-176-ms/4

https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/1233648/Short-and-Easy-Solution-w-Explanation-or-C%2B%2B-using-Bitset-and-Bit-masking-or-Beats-100

"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # solution 1: Time Limit Exceeded
        """ 
        def common(chars1, chars2):
            for c1, c2 in zip(chars1, chars2):
                if c1 and c2: return True
            return False
        chars = [[False]*26 for i in range(len(words))]
        res = 0
        for i, word in enumerate(words):
            for ch in word:
                chars[i][ord(ch) - ord('a')] = True
            for j in range(i):
                if not common(chars[i], chars[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
        """

        # solution 2: 
        d = {} 
        for w in words: 
            key = sum(1<<(ord(c) - ord('a')) for c in set(w))
            if key not in d:
                d[key] =len(w) 
            else:
                d[key] = max(d[key],len(w))
                
        res = 0
        for k1, v1 in d.items():
            for k2, v2 in d.items():
                if k1 & k2 == 0:
                    res = max(res, v1*v2)
        return res 
