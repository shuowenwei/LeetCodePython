# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/regular-expression-matching/

solution: https://leetcode.com/problems/regular-expression-matching/solution/


"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
#        if not p:
#            return not s
        # when p is empty, and then s is also empty, they match
        if p is None or len(p) == 0: 
            return s is None or len(s)  == 0 
        #first_match = bool(s) and p[0] in {s[0], '.'} 

        # s could be '' but '' is not None 
        first_match = (s is not None and len(s) > 0) and p[0] in {s[0], '.'} 
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:])) or (first_match and self.isMatch(s[1:], p))
        else: 
            return first_match and self.isMatch(s[1:], p[1:])