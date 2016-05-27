# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/plus-one/

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """
        stringNumber = ""
        for i in digits:
            stringNumber = stringNumber+str(i)
        results = str(int(stringNumber)+1) 
        return [int(e) for e in results]
        """
        
        #return [int(i) for i in str(int(''.join([str(i) for i in digits]))+1)]
        
        num = int("".join([str(i) for i in digits])) + 1
        return [int(i) for i in str(num)]