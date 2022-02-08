# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/palindrome-pairs/

https://leetcode.com/problems/palindrome-pairs/discuss/1269310/JS-Python-Java-C%2B%2B-or-Easy-Map-Matching-Solution-w-Explanation

"""
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """       
        def isPalindrome(word):
            left, right = 0, len(word) -1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        dict_map = {}
        for index, word in enumerate(words):
            dict_map[word] = index
            
        res = []
        for i, wi in enumerate(words): # words[i] is in front, words[j] in the back 
            if wi == '':
                for j in range(len(words)):
                    if isPalindrome(words[j]) and j != i:
                        res.append([i, j])
                        res.append([j, i])
                continue
                
            reverseWi = wi[::-1]
            if reverseWi in dict_map:
                if i != dict_map[reverseWi]:
                    res.append([i, dict_map[reverseWi] ])
            for j in range(1, len(reverseWi)): # can be empty string anymore ''
                if isPalindrome(reverseWi[:j]) and reverseWi[j:] in dict_map:
                    # if i == 1:
                    #     print(reverseWi[:j], reverseWi[j:])
                    #     print(isPalindrome(reverseWi[:j]), reverseWi[j:] in dict_map)
                    res.append([i, dict_map[reverseWi[j:]] ])
                if isPalindrome(reverseWi[j:]) and reverseWi[:j] in dict_map:
                    # if i == 1:
                    #     print(reverseWi[j:], reverseWi[:j])
                    #     print(isPalindrome(reverseWi[j:]), reverseWi[:j] in dict_map)
                    res.append([dict_map[reverseWi[:j]], i])
        return res


        # solution 2: long and ugly and Time Limit Exceeded 
        """
        res = []
        n = len(words)
        for i in range(n): # words[i] is in front, words[j] in the back 
            for j in range(n):
                if i != j:
                    wi, wj = words[i], words[j]
                    if len(wi) == len(wj):
                        if wi == wj[::-1]:
                            res.append([i, j])
                    elif len(wi) > len(wj):
                        k = len(wi) - len(wj)
                        wi_len = len(wi) - k/2
                        residual = (len(wi) - len(wj)) % 2
                        if wi[:wi_len - residual][::-1] == wi[wi_len:] + wj:
                            res.append([i, j])
                    elif len(wi) < len(wj):
                        k = (len(wj) - len(wi)) / 2 
                        residual = (len(wj) - len(wi)) % 2 
                        if wi + wj[:k] == wj[k:][residual:][::-1]:
                            res.append([i, j])
        return res
        """