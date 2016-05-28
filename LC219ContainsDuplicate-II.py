# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/contains-duplicate-ii/

"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
         
        if nums is None:
            return False
        d = {}
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[ nums[i] ] = i
            else: 
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[ nums[i] ] = i
        return False 
        """
    d = {}
    t = 0
    for i in xrange(len(nums)):
        t = nums[i]
        if not t in d or i-d[t] > k:
            d[t] = i
        else:
            return True
    return False
    """ 