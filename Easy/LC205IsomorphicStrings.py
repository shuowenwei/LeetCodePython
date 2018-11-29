# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/isomorphic-strings/

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        map_s = {} 
        map_t = {} 
        for ss, tt in zip(s, t):
            # must show up at the same time 
            if ss in map_s and tt in map_t: 
                if map_s[ss] != tt or map_t[tt] != ss:
                    return False 
            # must be no show at the same time 
            elif ss not in map_s and tt not in map_t: 
                map_s[ss] = tt 
                map_t[tt] =ss
            else:
                return False 
        return True 
                
        
