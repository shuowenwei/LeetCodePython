# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/divide-two-integers/

"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return sys.maxsize 
        res = 0 
        ncount = 0 
        neg = False  
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg = True 
        dividend = abs(dividend)
        divisor = abs(divisor)
        """
        if divisor == 1 and neg > 0: 
            return dividend
        if divisor == 1 and neg < 0:
            return - dividend
        """
        while dividend >= divisor:
            divisorExp = divisor 
            #dividend = dividend - divisor 
            ncount = 1 
            while dividend >= divisorExp: 
                dividend = dividend - divisorExp
                res = res + ncount
                divisorExp = divisorExp + divisorExp
                ncount = ncount + ncount
                
        if neg:
            if res < -2147483648:
                return -2147483648
            else: 
                return -res 
        else:
            if res > 2147483647: 
                return 2147483647
            else: 
                return res 
                
                