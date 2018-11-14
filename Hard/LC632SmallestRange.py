# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/smallest-range

solution explaination: https://www.youtube.com/watch?v=csJXQZFYklE

"""

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        import sys
        min_length = sys.maxsize 
        minx = 0 
        miny = sys.maxsize 
        listPointers = [0]*len(nums) 
        endFlag = False         
        for i in range(len(nums)):
            if endFlag:
                break
            for j in range(len(nums[i])):
                if endFlag:
                    break
                
                minValIndexNums, maxValIndexNums = 0, 0 # store which list in "nums" currently has the min/max value at the corresponding pointers in listPointers
                for k in range(len(nums)):
                    if nums[minValIndexNums][listPointers[minValIndexNums]] > nums[k][listPointers[k]]: 
                        minValIndexNums = k 
                    if nums[maxValIndexNums][listPointers[maxValIndexNums]] < nums[k][listPointers[k]]: 
                        maxValIndexNums = k
                #
                if miny - minx > nums[maxValIndexNums][listPointers[maxValIndexNums]] - nums[minValIndexNums][listPointers[minValIndexNums]]:
                    miny = nums[maxValIndexNums][listPointers[maxValIndexNums]]
                    minx = nums[minValIndexNums][listPointers[minValIndexNums]]
                    
                listPointers[minValIndexNums] += 1 
                if listPointers[minValIndexNums] == len(nums[minValIndexNums]):
                    endFlag = True
        return [minx, miny]
           
            
            