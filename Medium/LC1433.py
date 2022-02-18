# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/check-if-a-string-can-break-another-string/

"""
class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # my solution: O(nlogn)
        s1 = sorted(list(s1))
        s2 = sorted(list(s2))
        res = []
        for ss1, ss2 in zip(s1, s2):
            if ord(ss1) < ord(ss2):
                res.append('s2')
            if ord(ss1) > ord(ss2):
                res.append('s1')
            if ord(ss1) == ord(ss2):
                res.append('0')
        if 's1' in set(res) and 's2' in set(res):
            return False
        return True


# https://leetcode.com/problems/check-if-a-string-can-break-another-string/discuss/608668/Python-O(n).
class Solution(object):
    def check(self, d1, d2):
        s = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            s += d1[c] - d2[c]
            if s < 0: # > works too
                return False
        return True
    
    def checkIfCanBreak(self, s1, s2):
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)
        return self.check(d1, d2) | self.check(d2, d1)