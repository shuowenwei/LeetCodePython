# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/find-k-closest-elements/

https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)

LC215, LC973, LC658
"""
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]
        if k >= len(arr):
            return arr
        
        res = []
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left ) / 2
            if x - arr[mid] > arr[mid + k] - x: 
                left = mid + 1
            else:
                right = mid 
        return arr[left : left + k]

    
