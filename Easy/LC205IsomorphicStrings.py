# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/isomorphic-strings/

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False 
        
        HashMap_s = {} 
        HashMap_t = {} 
        for i in range(len(s)):
            if s[i] in HashMap_s and t[i] in HashMap_t: 
                if HashMap_s[s[i]] != t[i] or HashMap_t[t[i]] != s[i]:
                    return False 
            elif s[i] not in HashMap_s and t[i] not in HashMap_t:
                HashMap_s[s[i]] = t[i] 
                HashMap_t[t[i]] = s[i]
            else:
                return False 
        return True
        
