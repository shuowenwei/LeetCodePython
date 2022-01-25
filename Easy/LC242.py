# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-anagram/

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        for ss in s:
            if ss in dict_s:
                dict_s[ss] += 1
            else:
                dict_s[ss] = 1 
                
        for tt in t:
            if tt not in dict_s:
                return False
            else:
                dict_s[tt] -= 1
                if dict_s[tt] < 0:
                    return False
                elif dict_s[tt] == 0:
                    del dict_s[tt]
        return len(dict_s) == 0 
    
        # solution 2: O(nlog(n))
        # return "".join(sorted(list(s))) == "".join(sorted(list(t)))
        
        # solution 3: 
        # return set(s) == set(t) and map(s.count,sorted(list(set(s)))) == map(t.count,sorted(list(set(s))))