# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

LC39, LC40, LC1239
"""
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.res = 0
        charCounter = [0] * 26
        if len(arr) == 0:
            return 0 
        def backtracking(arr, start, path):
            # print(path, start, ''.join(path), len(''.join(path)))
            combine = ''.join(path)
            if len(combine) != len(set(combine)):
                return
            self.res = max(self.res, len(combine))
            if start == len(arr):
                return
            for i in range(start, len(arr)):
                flag = False
                for char in arr[i]:
                    if charCounter[ord(char) - ord('a')] >= 1:
                        flag = True
                        break 
                if flag:
                    continue
                path.append(arr[i])
                for char in arr[i]:
                    charCounter[ord(char) - ord('a')] += 1 
                backtracking(arr, i + 1, path)
                tmp = path.pop()
                for char in tmp:
                    charCounter[ord(char) - ord('a')] -= 1 
        backtracking(arr, 0, [])
        return self.res
    
    
    # solution 2: refer to: 
        self.res = 0
        if len(arr) == 0:
            return 0 
        def backtracking(arr, start, path):
            # print(path, start, ''.join(path), len(''.join(path)))
            if len(path) != len(set(path)):
                return
            self.res = max(self.res, len(path))
            if start == len(arr):
                return
            for i in range(start, len(arr)):
                backtracking(arr, i + 1, path + arr[i])
        backtracking(arr, 0, '')
        return self.res