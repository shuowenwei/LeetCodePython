# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/top-k-frequent-elements/

LC215, LC973, LC658, LC347
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        c = Counter(nums)
        freq = [(freq, key) for key, freq in c.items()]
        
        def helper(freq, k, res):
            if k <= 0:
                return res
            random.shuffle(freq)
            pivot = freq[0][0]
            left = [d for d in freq if d[0] < pivot]
            equals = [d for d in freq if d[0] == pivot]
            right = [d for d in freq if d[0] > pivot]
            if k <= len(right):
                return helper(right, k, res)
            elif k - len(right) <= len(equals):
                res += [ val for freq, val in right + equals]
                return helper(equals, k - len(right + equals), res)
            else:
                res += [ val for freq, val in right + equals]
                return helper(left, k - len(right + equals), res)
            
        res = helper(freq, k, [])
        return res 