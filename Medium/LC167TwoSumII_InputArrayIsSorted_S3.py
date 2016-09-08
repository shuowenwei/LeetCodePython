# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

https://discuss.leetcode.com/topic/56486/python-skipping-duplicates-before-binary-search

Noticed that test cases contain duplicate numbers. So, skipping duplicates made the code run much faster. Even beat 100% (run time 36 ms) once (in a blue moon).


"""
class Solution(object):
    def twoSum(self, numbers, target):
        for i in xrange(len(numbers)):
            if i > 0 and numbers[i-1] == numbers[i]:
                continue
            l = i + 1
            r = len(numbers) - 1
            while (l <= r):
                mid = (l + r) / 2
                if target - numbers[i] == numbers[mid]:
                    return [i + 1, mid + 1]
                elif target - numbers[i] < numbers[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

