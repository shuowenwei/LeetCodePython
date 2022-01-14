# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/string-to-integer-atoi/

https://leetcode.com/problems/string-to-integer-atoi/discuss/798380/Fast-and-simpler-DFA-approach-(Python-3)

"""
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        digits = set('0123456789')
        if len(s) == 0:
            return 0
        val, pos = 0, 0
        sign = 1
        flag = 'non_digit'
        hasSign = False 
        while pos < len(s):
            curr_char = s[pos]
            if flag == 'non_digit':
                if curr_char == ' ':
                    flag = 'non_digit'
                elif curr_char in ('+', '-'):
                    flag = 'has_sign'
                    if curr_char == '-':
                        sign = -1 
                elif curr_char in digits:
                    val = val*10 + int(curr_char)
                    flag = 'digit'
                else:
                    return 0
            elif flag == 'has_sign':
                if curr_char in digits:
                    flag = 'digit'
                    val = val*10 + int(curr_char)
                else:
                    break
            elif flag == 'digit':
                if curr_char in digits:
                    val = val*10 + int(curr_char)
                else:
                    break
            else:
                break
            pos += 1 
        val = val*sign
        val = min(val, 2**31-1)
        val = max(val, -2**31)
        return val
    
        """ my solution long ago: 
        res = '0'  #    int('0021') = 21 
        if '+' in str and '-' in str:   # input = '+-2'
            return 0 
        strip_str = str.strip(" ")
        isNegative = False
        
        if len(strip_str) == 0:
            return 0 
            
        if len(strip_str) > 0 and strip_str[0] == "+":
            strip_str = strip_str[1:]   # input = "  +  413"  or  "    010" or " ++1"
            
        if len(strip_str) > 0 and strip_str[0] == "-":
            isNegative = True
            strip_str = strip_str[1:]   # input = '  - 321'
            
        if len(strip_str) == 0:  # input = '-'
            return 0 
            
        for e in strip_str:
            if e in "0123456789":
                res += e
            else:
                break
            
        if isNegative:
            return max(-int(res),-2147483648)
        else:
            return min(int(res),2147483647)
        """

