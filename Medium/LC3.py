# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/longest-substring-without-repeating-characters/

labuladong: https://labuladong.gitee.io/algo/1/9/

solution: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1781/Python-solution-with-comments. 

https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # just use the template
        res = 0 
        tmp_len = 0 
        window = {char: 0 for char in s}
        left, right = 0, 0 
        valid = 0
        while right < len(s): 
            c = s[right]
            right += 1
            window[c] += 1
            tmp_len += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
                tmp_len -= 1
            res = max(res, tmp_len) 
        return res
        """
        maxSubstringLen = 0
        start = 0 
        dictChar = {} 
        if not s:
            return maxSubstringLen
        for i in range(len(s)):
            if s[i] in dictChar:
                maxSubstringLen = max(maxSubstringLen, i - start)
                start = max(start, dictChar[s[i]] + 1) # be careful: 'abba'
            dictChar[s[i]] = i
        maxSubstringLen = max(maxSubstringLen, len(s) - start)
        return maxSubstringLen 
        """
        
        """
        maxSubstringLen = 0
        start = 0 
        dictChar = {} 
        if not s:
            return maxSubstringLen
        for i in range(len(s)):
            if s[i] in dictChar:# and start <= dictChar[s[i]]:
                start = max(dictChar[s[i]] + 1, start) 
                maxSubstringLen = max(maxSubstringLen, i - start + 1)
            else:
                maxSubstringLen = max(maxSubstringLen, i - start + 1)
            dictChar[s[i]] = i 
        return maxSubstringLen 
        """