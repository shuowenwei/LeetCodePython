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
        
        dict_letter2index = {}
        for letter in set(s):
            dict_letter2index[letter] = [-1, -1]
        
        res = 0
        for i, letter in enumerate(s):
            start, end = dict_letter2index[letter]
            res += (i - end) * (end - start)
            dict_letter2index[letter] = [end, i]
            
        for letter, index_positions in dict_letter2index.items():
            start, end = index_positions
            res += (len(s) - end) * (end - start)
        return res 