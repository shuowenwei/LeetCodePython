# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/string-compression/

LC443, LC1868
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        if n < 2:
            return n 
        slow, fast = 0 , 0
        n = len(chars)
        count = 0
        res = ''
        while fast < n:
            if chars[fast] == chars[slow]:
                count += 1
                fast += 1
            else:
                res += chars[slow]
                if count > 1:
                    res += str(count)
                else:
                    pass 
                slow = fast
                count = 1 
                fast += 1
        if fast != slow:
            res += chars[slow]
            if count > 1:
                res += str(count)
        
        for i, c in enumerate(res):
            chars[i] = c
        return len(res)
