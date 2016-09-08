# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for small_index in range(len(numbers)): 
            #print("small=",small_index)
            big_index = self.findRemain(numbers, small_index+1, target-numbers[small_index])
            if big_index is not None:
                return [small_index+1, big_index+1]
            else:
                continue 
            
    def findRemain(self, numbers, small_index, r):
        if r < 0 or r > numbers[-1]:
            return None 
            
        big_index = len(numbers) 
        mid = (small_index+big_index)/2
        while small_index <= big_index:
            if numbers[mid] > r: 
                big_index = mid - 1 
            elif numbers[mid] < r:
                small_index = mid + 1
            else:
                return mid
            #print("m,s,b=",mid, small_index,big_index)
            mid = (small_index+big_index)/2
 
        return None 
"""
some test cases: 
[5,25,75]
100

[3,24,50,79,88,150,345]
200

[0,0,3,4]
0

"""
