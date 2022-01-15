# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number-iii/

LC136, LC137, LC260
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict_stack = {}
        for n in nums:
            if n in dict_stack:
                del dict_stack[n]
            else:
                dict_stack[n] = 0 
        return list(dict_stack)

        # solution 2: used too much space 
        hashMap = dict()
        for e in nums:
            if e in hashMap:
                hashMap[e] += 1
            else:
                hashMap[e] = 1
        res = []
        for key,value in hashMap.items():
            if value == 1:
                res.append(key)
        return res 