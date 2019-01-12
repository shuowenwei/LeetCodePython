# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/subarray-sum-equals-k

solution: https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book

"""
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running_sum = 0
        hash_table = dict()
        #hash_table = collections.defaultdict(lambda:0,hash_table)
        total = 0
        for x in nums:
            running_sum += x # the sum from nums[0:x_index]
            sum = running_sum - k            
            if running_sum not in hash_table:
                hash_table[running_sum] = 0
                
            if sum in hash_table:
                total += hash_table[sum]
                
            if sum == 0:
                total += 1
        
            hash_table[running_sum] += 1 
        
        return total

        