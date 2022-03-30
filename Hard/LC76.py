# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-window-substring/

https://labuladong.gitee.io/algo/1/9/

LC76, LC567, LC438, LC30
"""
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        
        need = {char: t.count(char) for char in t}
        window = {char: 0 for char in t}
        left, right = 0, 0 
        valid = 0
        match_start = 0
        match_length = 2**31 - 1
        while right < len(s): 
            c = s[right]
            right += 1 
            if c in need: # A.K.A: c in window:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            # print(left, right, valid, len(need),need, window, s[match_start: match_start + match_length])
            while valid == len(need):
                if right - left < match_length:
                    match_start = left
                    match_length = right - left
                d = s[left]
                left += 1
                if d in need: # A.K.A: d in window:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if match_length == 2**31 - 1  else s[match_start: match_start + match_length]
    
    