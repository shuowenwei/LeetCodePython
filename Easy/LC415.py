# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-strings/

LC415, LC43
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_n1, lenn2 = len(num1), len(num2)
        lst_num1, lst_num2 = list(num1), list(num2)
        res = []
        carry = 0 
        while lst_num1 and lst_num2:
            tmp = int(lst_num1.pop()) + int(lst_num2.pop()) + carry 
            carry = tmp / 10 
            res.append(tmp % 10)
            
        while lst_num1:
            tmp = int(lst_num1.pop()) + carry 
            carry = tmp / 10 
            res.append(tmp % 10)
        
        while lst_num2:
            tmp = int(lst_num2.pop()) + carry 
            carry = tmp / 10 
            res.append(tmp % 10)
        if carry > 0:
            res.append(carry)
        return ''.join([str(i) for i in res[::-1]])
