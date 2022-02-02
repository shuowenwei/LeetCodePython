# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

http://mlwiki.org/index.php/Gram_Matrices

labuladong: https://labuladong.gitee.io/algo/1/9/

lC76, LC567, LC438, LC3

"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        t = p
        res = []
        need = {char: t.count(char) for char in t}
        window = {char: 0 for char in t}
        left, right = 0, 0 
        valid = 0
        while right < len(s): 
            c = s[right]
            right += 1 
            if need.get(c) is not None:
                if c in window: 
                    window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            else:
                left = right 
                window = {char: 0 for char in t}
                valid = 0
            while right - left >= len(t):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if need.get(d) is not None:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
                

        # my other ugly solution 
        window_size = len(p)
        dict_s = collections.defaultdict(lambda : 0)
        dict_p = collections.defaultdict(lambda : 0)
        for char in p:
            dict_p[char] += 1
        i, j = 0, 0
        res = []
        while j < len(s):
            char = s[j]
            if char not in dict_p:
                i = j
                dict_s = collections.defaultdict(lambda : 0)
            else:
                dict_s[char] += 1
            if j - i + 1 == window_size:
                # print(i, j, dict_s)
                if dict_p == dict_s:
                    res.append(i)
                if s[i] in dict_s:    # these two rows 
                    dict_s[s[i]] -= 1 # are important 
                i += 1
            j += 1
        return res 