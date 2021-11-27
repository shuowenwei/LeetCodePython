# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

http://mlwiki.org/index.php/Gram_Matrices

labuladong: https://labuladong.gitee.io/algo/1/9/

"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        t = p
        res = []
        need = {char: t.count(char) for char in t}
        window = {char: 0 for char in t}
        left, right = 0, 0 
        valid = 0
        while right < len(s): 
            c = s[right]
            right += 1 
            if need.get(c) is not None:
                if c in window: 
                    window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            else:
                left = right 
                window = {char: 0 for char in t}
                valid = 0
            while right - left >= len(t):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if need.get(d) is not None:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
                
