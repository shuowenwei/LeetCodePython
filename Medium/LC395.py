# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

solution reference: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/139609/python-iterative-and-recursive-solution

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/492483/Python-short-and-clean

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/949688/Python-Short-and-Simple-Recursive-Solution

"""
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict_count = {}
        for ss in s:
            if ss not in dict_count:
                dict_count[ss] = 1
            else:
                dict_count[ss] += 1
        maxLength = 0
        st = 0
        # print(st, maxLength)
        for i, char in enumerate(s):
            if dict_count[char] < k:
                maxLength = max(maxLength, self.longestSubstring(s[st:i], k))
                st = i + 1
        if st == 0:
            return len(s)
        else:
            return max(maxLength, self.longestSubstring(s[st:], k))

        
        # solution 1: split into left and right, slow!!!!
        from collections import Counter
        if len(s) == 0 or k > len(s):
            return 0
        c = Counter(s)
        for i, letter in enumerate(s):
            if c[letter] < k:
                leftLength = self.longestSubstring(s[:i], k)
                rightLength = self.longestSubstring(s[i+1:], k)
                return max(leftLength, rightLength)
                # break
        # else:
        return len(s)
        # return max(leftLength, rightLength)


        """ 
        # solution 3 recursive 
        res = 0 
        if not s or len(s) < k:
            return res 
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        # if every char in s appears >= k time, then the whole string is OK 
        return len(s)
        """
        