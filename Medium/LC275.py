# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/h-index-ii/

LC275
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left = 0
        right = len(citations) - 1 
        while left <= right: 
            mid = left + (right - left) / 2
            if citations[mid] >= len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1 
        return len(citations)-left 
