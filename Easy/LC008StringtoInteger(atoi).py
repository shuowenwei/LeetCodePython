# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/string-to-integer-atoi/


Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
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