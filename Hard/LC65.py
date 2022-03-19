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
        dotFlag = False
        eFlag = False
        digitFlag = False
        for i, char in enumerate(s):
            if char in ('+', '-'):
                if i == 0:
                    continue 
                elif i > 0 and s[i-1] not in ('e','E'):
                    return False
            elif not char.isdigit() and char not in ('e','E','.'): 
                return False
            elif char in ('e','E'):
                # can't have more than 1 e/E, must have digit before 
                if eFlag is True or digitFlag is False:
                    return False
                eFlag = True
                digitFlag = False # must reset to False, corner case: '0e'
            elif char in ('.'):
                 # can't have more than 1 dot, after e/E it must be integer
                if dotFlag is True or eFlag is True:
                    return False
                dotFlag = True 
            elif char.isdigit():
                digitFlag = True
                
        return digitFlag # corner case: '.'
