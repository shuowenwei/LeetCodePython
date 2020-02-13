# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/ransom-note/

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_magazine = {} 
        for element in magazine:
            if element not in dict_magazine: 
                dict_magazine[element] = 1
            else:
                dict_magazine[element] += 1
        
        for e in ransomNote:
            if e not in dict_magazine:
                return False 
            else:
                dict_magazine[e] -= 1 
                if dict_magazine[e] < 0:
                    return False 
        return True 