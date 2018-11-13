# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

http://mlwiki.org/index.php/Gram_Matrices

a good solution: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92009/Python-Sliding-Window-Solution-using-Counter

"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter 
        res = [] 
        
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1 
            if sCounter == pCounter: 
                res.append(i-len(p)+1)
                
            sCounter[ s[i-len(p)+1] ] -= 1 
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return res 
                
