# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/minimum-window-substring/

"""
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        if len(s) < len(t):
            return ''
        
        tCounter = Counter(t) 
        match_cnt = 0 
        match_start = 0
        match_length = sys.maxsize 
        slow = 0 
        for fast in range(len(s)):
            if s[fast] not in tCounter:
                continue
            if tCounter[s[fast]] == 1: 
                match_cnt += 1
            tCounter[s[fast]] = tCounter[s[fast]] - 1
            
            while (match_cnt == len(tCounter)):
                # find a validate substring 
                if fast - slow + 1 < match_length:
                    match_length = fast - slow + 1 
                    match_start = slow
                leftMost = slow 
                slow += 1
                if s[leftMost] not in tCounter:
                    continue 
                tCounter[s[leftMost]] = tCounter[s[leftMost]] + 1
                if tCounter[s[leftMost]] > 0: 
                    match_cnt -= 1 
        if match_length == sys.maxsize:
            return ''
        return s[match_start: match_start+match_length]
    
    