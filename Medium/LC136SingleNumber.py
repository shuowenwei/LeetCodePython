# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

httpsleetcode.comproblemssingle-number

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashSet = set()
        for e in nums:
            if e in hashSet: 
                hashSet.remove(e)
            else:
                hashSet.add(e)
        return hashSet.pop()