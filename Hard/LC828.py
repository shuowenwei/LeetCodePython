# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/128952/C%2B%2BJavaPython-One-pass-O(N)

"""
class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_char2index = {}
        for char in set(s):
            dict_char2index[char] = [-1, -1]
        
        res = 0
        for i, c in enumerate(s):
            start, end = dict_char2index[c]
            res += (i - end) * (end - start)
            dict_char2index[c] = [end, i]

        for c, index_positions in dict_char2index.items():
            start, end = index_positions
            res += (len(s) - end) * (end - start)
        return res 