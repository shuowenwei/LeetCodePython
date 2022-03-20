# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/group-shifted-strings/

https://techyield.blogspot.com/2020/10/group-shifted-strings-python-solution.html
"""
class Solution(object):
    def groupStrings(self, strings):
        """
        List[str]
        List[List[str]]
        """
        import collections
        groups = collections.defaultdict(list)
        for s in strings:
            key = ()
            for i in range(len(s)-1):
                key += ((26 + ord(s[i+1]) - ord(s[i])) % 26,)
                
            groups[key].append(s)
            
        return groups.values()
