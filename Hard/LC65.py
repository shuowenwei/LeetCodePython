# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-number/

"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if len(s.split('.')) > 2 or len(s.split('e')) > 2:
        #     return False
        # corner cases: '.', 'e', '0e', '1e', '005047e+6'
        dotFlag, eFlag, digitFlag = False, False, False
        for i, char in enumerate(s):
            if char in ('+', '-'):
                if i == 0:
                    continue
                elif i > 0 and s[i-1] != 'e':
                    return False
            elif not char.isdigit() and char not in ('.', 'e', 'E'):
                return False 
            elif char in ('e', 'E'):
                if eFlag or digitFlag is False: 
                    return False
                eFlag = True
                digitFlag = False
            elif char == '.':
                if dotFlag == True or eFlag == True:
                    return False
                dotFlag = True
            elif char.isdigit():
                digitFlag = True
                
        return digitFlag
