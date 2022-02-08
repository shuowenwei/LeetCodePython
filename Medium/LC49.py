# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/group-anagrams/

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_word_index = collections.defaultdict(list)
        for i, w in enumerate(strs):
            sort_w = ''.join(sorted(w))
            dict_word_index[sort_w].append(i)
        res = []
        for _, indices in dict_word_index.items():
            tmp = [strs[i] for i in indices]
            res.append(tmp)
        return res
    
        # longer version, Time Limit Exceeded
        """
        from collections import Counter 
        dict_word_len = collections.defaultdict(list)
        for w in strs:
            dict_word_len[len(w)].append(w)
        
        def isAnagram(a, b):
            return Counter(a) == Counter(b)
        
        res = []
        for length, list_words in dict_word_len.items():
            visited = set()
            for i in range(len(list_words)):
                if i not in visited:
                    tmp = [list_words[i]]
                    visited.add(i)
                    for j in range(len(list_words)):
                        if i != j and j not in visited and isAnagram(list_words[i], list_words[j]):
                            tmp.append(list_words[j])
                            visited.add(j)
                    res.append(tmp)
        return res
        """