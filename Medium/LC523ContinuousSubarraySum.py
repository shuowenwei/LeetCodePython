# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/continuous-subarray-sum/

solution: https://leetcode.com/problems/continuous-subarray-sum/discuss/99566/Simple-Python-(10-lines)-with-Explanation-58ms-O(n)-time-O(k)-space

"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if k == 0:
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
        if len(nums) < 2:
            return False 
        k = abs(k)
        modDict = {0: -1} # must initialize a mod value: 0 
        cumSumModK = 0 
        for i, n in enumerate(nums):
            cumSumModK =  (cumSumModK + n ) % k
            if cumSumModK in modDict and i - modDict[cumSumModK] > 1: 
                return True 
            if cumSumModK not in modDict: 
                modDict[cumSumModK] = i
        return False

        """ 
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i-1] ==0 and nums[i] == 0:
                    return True
            else:
                return False
        if len(nums) < 2: 
            return False
        k = abs(k)
        sumList = [0] * len(nums) 
        sumList[0] = nums[0]
        for i in range(1, len(nums)):
            sumList[i] = sumList[i-1] + nums[i]
            
        if sumList[-1] % k == 0 and len(sumList) >= 2:
            return True 
        #sumList = [0] + sumList  
        for i in range(len(sumList)): 
            for j in range(i+1, len(sumList)): 
                if (sumList[j] - sumList[i]) % k == 0 and (j-i) > 1:
                    return True 
        return False
        """