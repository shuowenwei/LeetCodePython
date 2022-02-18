# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/string-compression/

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
        fast, slow = 0, 0
        res = 0
        count = 0
        while fast < n:
            # print(fast, slow, chars[fast], chars[slow], count)
            if chars[fast] == chars[slow]:
                count += 1
            else:
                chars[res] = chars[slow]
                res += 1
                if count > 1:
                    for k in range(len(str(count))):
                        print(k, count)
                        chars[res] = list(str(count))[k]
                        res += 1
                slow = fast
                count = 1
            fast += 1
            
        if fast == n:
            chars[res] = chars[slow]
            res += 1
            if count > 1:
                for k in range(len(str(count))):
                    chars[res] = list(str(count))[k]
                    res += 1
        return res
