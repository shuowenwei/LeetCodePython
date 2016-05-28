# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/contains-duplicate/

"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #newList = []
        newSet = set()
        for e in nums: 
            if e not in newSet:
                newSet.add(e)
            else:
                return True
        return False 