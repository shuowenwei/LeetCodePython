# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/array-of-doubled-pairs/

LC954, LC2007
"""
import collections
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # solution 1: O(NlogK)
        # https://leetcode.com/problems/array-of-doubled-pairs/discuss/203183/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100
        dctNum2Count = collections.defaultdict(int)
        for a in arr:
            dctNum2Count[a] += 1
        
        for c in sorted(dctNum2Count.keys(), key = abs):
            if dctNum2Count[c] > dctNum2Count[c*2]:
                return False
            dctNum2Count[c*2] -= dctNum2Count[c]
        return True


        # solution 2: O(NlogN)
        # https://leetcode.com/problems/array-of-doubled-pairs/discuss/1396805/Python-O(n-log-n)-greedy-solution-explained
        dctNum2Count = collections.defaultdict(int)
        for a in arr:
            dctNum2Count[a] += 1
        
        arr.sort(key = lambda x: abs(x))
        for a in arr: 
            if dctNum2Count[a] == 0:
                continue
            if 2*a not in dctNum2Count or dctNum2Count[2*a] == 0:
                return False
            dctNum2Count[2*a] -= 1
            dctNum2Count[a] -= 1
        return True