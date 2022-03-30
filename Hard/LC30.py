# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-window-substring/

LC76, LC30
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        single_len = len(words[0])
        total_len = len(words[0]) * len(words)
        res = []
        n = len(s)
        need = {w: words.count(w) for w in words}
        have = {w: 0 for w in words}
        right = 0
        while right < n - total_len + 1:
            window = s[right: right + total_len]
            have = {w: 0 for w in words}
            valid = 0
            for i in range(0, total_len, single_len):
                cw = window[i: i+single_len]
                if cw not in need:
                    break
                else:
                    have[cw] += 1
                    if have[cw] == need[cw]:
                        valid += 1
            if valid == len(need):
                res.append(right)
            #     right += single_len
            # else:
            # "aaaaaaaaaaaaaa"
            # ["aa","aa"]
            right += 1
        return res 
            
            