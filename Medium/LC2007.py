# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/array-of-doubled-pairs/

https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100

LC954, LC2007
"""
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2 != 0:
            return []
        
        dctNum2Count = collections.defaultdict(int)
        for a in changed:
            dctNum2Count[a] += 1
            
        if dctNum2Count[0] % 2 != 0:  # [0,0,0] -> []
            return []
        
        for c in sorted(dctNum2Count.keys()):
            if dctNum2Count[c] > dctNum2Count[c*2]:
                return []
            if c == 0:  # [0,0,0,0] -> [0,0]
                dctNum2Count[0] -= dctNum2Count[0] // 2
            else:
                dctNum2Count[c*2] -= dctNum2Count[c]
        res = []
        for n, cnt in dctNum2Count.items():
            if cnt > 0:
                res = res + [n] * cnt
        return res 
        # return [n for n, cnt in dctNum2Count.items() if cnt > 0 and n != 0] + [0] * dctNum2Count[0]
