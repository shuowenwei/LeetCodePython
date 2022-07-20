# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-matching-subsequences/

LC392, LC792
"""
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        
        # Time Limit Exceeded
        # refer to LC392
        def isSubsequence(word, s):
            pw, ps = 0, 0 
            while pw < len(word) and ps < len(s):
                if word[pw] == s[ps]:
                    pw += 1
                    ps += 1
                else:
                    ps += 1 
            return pw == len(word)
        
        res = 0 
        for word in words:
            if isSubsequence(word, s):
                res += 1
        return res 
        
        
        

