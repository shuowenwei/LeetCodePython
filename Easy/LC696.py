# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-binary-substrings/

https://leetcode.com/problems/count-binary-substrings/discuss/1172569/Short-and-Easy-w-Explanation-and-Comments-or-Keeping-Consecutive-0s-and-1s-Count-or-Beats-100

"""
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace('01', '0 1').replace('10', '1 0')
        consective_01_len = [len(seg) for seg in s.split()]
        res = [min(a,b) for a,b in zip(consective_01_len, consective_01_len[1:])]
        return sum(res)
