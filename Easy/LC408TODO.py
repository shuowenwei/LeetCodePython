# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/valid-word-abbreviation/

"""
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        pointer = 0
        num = 0
        for ab in abbr: 
            if ab.isdigit():
                if int(ab) == 0 and num == 0: # 10 is ok 
                    return False
                num = num * 10 + int(ab)
            else:
                pointer += num 
                num = 0 
                if pointer >= len(word) or word[pointer] != ab:
                    return False
                # when matched, pointer must move to next
                pointer += 1
        return num + pointer == len(word) - 1 
"""
Example 1:
Given s = "i nternational ization", abbr = "i12iz4n":
Return true.

ab: i 12 i z 
pointer: 0 12 13 14 
word[pointer]: i i z


Example 2:
Given s = "apple", abbr = "a2e":
Return false.
"""