# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/add-digits/

"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        while num >= 10: 
            temp = 0 
            while num > 0:
                temp = temp + num%10
                num = num / 10 
            num = temp 
        return num
        """
        if num < 10: 
            return num 
        else: 
            temp = 0
            while num > 0:
                temp+=num%10
                num = num/10
            return self.addDigits(temp)
        