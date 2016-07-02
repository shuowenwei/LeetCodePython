# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/single-number-iii/

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
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
