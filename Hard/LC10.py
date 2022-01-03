# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/regular-expression-matching/

solution: https://leetcode.com/problems/regular-expression-matching/solution/

https://labuladong.gitee.io/algo/3/26/88/
https://mp.weixin.qq.com/s/rnaFK05IcFWvNN1ppNf2ug

LC10
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
            # 1st part: when p[1] is *, p[0] is ., s='abcde', p='.*ade'
            # 2nd part: when p[1] is *, s='aaabc', p='a*bc' 
            return (self.isMatch(s, p[2:])) or (first_match and self.isMatch(s[1:], p))
        else: 
            return first_match and self.isMatch(s[1:], p[1:])
        
        # solution 2:
        """
        dp_table = {}
        def dp(s, p, i, j):
            # base case:
            if j == len(p):
                return i == len(s)
            if i == len(s):
                if (len(p) - j) % 2 == 1:
                    return
                while j+1 < len(p):
                    if p[j+1] != '*':
                        return False 
                    j += 2 
                return True
            
            # check s[i] p[j] match
            if (i,j) in dp_table:
                return dp_table[(i,j)]
            res = False
            if s[i] == p[j] or p[j] == '.':
                if j < len(p)-1 and p[j+1] == '*':
                    res = dp(s, p, i, j+2) or dp(s, p, i+1, j)
                else:
                    res = dp(s, p, i+1, j+1)
            else:
                if j < len(p)-1 and p[j+1] == '*':
                    res = dp(s, p, i, j+2)
                else:
                    res = False
            dp_table[(i,j)] = res
            return res
        return dp(s, p, 0, 0)
        """