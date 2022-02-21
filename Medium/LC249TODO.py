# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/group-shifted-strings/

https://www.geeksforgeeks.org/group-shifted-string/

"""
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if len(strings) == 0:
            return []

        str_map = dict()
        for s in strings:
            delta = ord(s[0]) - ord('a')
            key = "".join([chr(ord(c) - delta) if c >= s[0] else chr(26 + ord(c) - delta) for c in s])
            if k not in str_map:
                str_map[key] = []
            else:
                str_map[key].append(s)

        return str_map.values()