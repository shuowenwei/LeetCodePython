# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/regular-expression-matching/

solution: https://leetcode.com/problems/regular-expression-matching/solution/

https://labuladong.gitee.io/algo/3/25/88/
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
        # solution 1: 
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
        
        # solution 2: dp
        """ 
        dp_table = {}
        # 若dp(s,i,p,j) = true，则表示s[i..]可以匹配p[j..]；
        # 若dp(s,i,p,j) = false，则表示s[i..]无法匹配p[j..]。
        def dp(s, p, i, j):
            # base case:
            if j == len(p):
                return i == len(s)
            if i == len(s): # example: s="a", p="ab*c*"   # *: 0 or more
                # // 如果能匹配空串，一定是字符和 * 成对儿出现
                if (len(p) - j) % 2 == 1:
                    return False
                # // 检查是否为 x*y*z* 这种形式
                while j+1 < len(p):
                    if p[j+1] != '*':
                        return False 
                    j += 2 
                return True
            
            # check if s[i] and p[j] match
            if (i,j) in dp_table:
                return dp_table[(i,j)]
            res = False
            if s[i] == p[j] or p[j] == '.': # 通配符匹配 0 次或多次
                if j < len(p)-1 and p[j+1] == '*':
                    # 将j加 2，i不变，含义就是直接跳过p[j]和之后的通配符，即通配符匹配 0 次：
                    # 将i加 1，j不变，含义就是p[j]匹配了s[i]，但p[j]还可以继续匹配，即通配符匹配多次的情况：
                    res = dp(s, p, i, j+2) or dp(s, p, i+1, j)
                else:
                    # 由于这个条件分支是无*的常规匹配，那么如果s[i] == p[j]，就是i和j分别加一：
                    res = dp(s, p, i+1, j+1)
            else: #通配符匹配 0 次
                if j < len(p)-1 and p[j+1] == '*':
                    # 将j加 2，i不变，含义就是直接跳过p[j]和之后的通配符，即通配符匹配 0 次：
                    res = dp(s, p, i, j+2)
                else:
                    # 如果没有*通配符，也无法匹配，那只能说明匹配失败了：
                    res = False
            dp_table[(i,j)] = res
            return res
        return dp(s, p, 0, 0)

        """