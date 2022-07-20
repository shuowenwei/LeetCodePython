# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/number-of-matching-subsequences/

LC392, LC792
"""
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # solution 1: Binary Search
        def left_bound(nums, target):
            left = 0
            right = len(nums) - 1 
            while left <= right: # break when left == right + 1 
                mid = left + (right - left) / 2 
                if nums[mid] == target:
                    right = mid - 1 
                elif nums[mid] < target:
                    left = mid + 1 
                elif nums[mid] > target:
                    right = mid - 1
            # if left > len(nums) - 1  or nums[left] != target: 
            #     return -1 
            return left
        
        
        dict_s = {}
        for i, char in enumerate(s):
            if char in dict_s:
                dict_s[char].append(i)
            else:
                dict_s[char] = [i]
                
        def isSubsequence(word, s):
            ps = 0 # pointer on s 
            for w in word:
                if w not in dict_s:
                    return False 
                
                pos = left_bound(dict_s[w], ps)
                if pos == len(dict_s[w]):
                    return False
                ps = dict_s[w][pos] + 1 
            return True
    
        res = 0 
        for word in words:
            if isSubsequence(word, s):
                res += 1
        return res 
        
        
        # Solution 2: Time Limit Exceeded
        # refer to LC392
        def isSubsequence(word, s):
            pw, ps = 0, 0 
            while pw < len(word) and ps < len(s):
                if word[pw] == s[ps]:
                    pw += 1
                    ps += 1
                else:
                    ps += 1 
            return pw == len(word)
        
        res = 0 
        for word in words:
            if isSubsequence(word, s):
                res += 1
        return res 
        
        
        

