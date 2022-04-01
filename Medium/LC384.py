# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/shuffle-an-array/

LC384, LC46, LC47
"""
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.org_nums = nums
    def reset(self):
        """
        :rtype: List[int]
        """
        return self.org_nums
    
    # Fisher-Yates algorithm, explained
    def shuffle(self): # https://leetcode.com/problems/shuffle-an-array/discuss/1350213/Python-Fisher-Yates-algorithm-explained
        """
        :rtype: List[int]
        """
        res = self.org_nums[:]
        n = len(self.org_nums)
        for i in range(n):
            j = random.randint(i, n-1)
            res[i], res[j] = res[j], res[i]
        return res 
    
# solution 2: backtracking
class Solution(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.org_nums = nums
        self.shuffles = []
        visited_index = [False] * len(nums)
        # refer to LC46
        def backtracking(arr, path):
            if len(path) == len(arr):
                if path != self.org_nums:
                    self.shuffles.append(path[:])
                return 
            for i in range(len(nums)):
                if visited_index[i]:
                    continue
                path.append(nums[i])
                visited_index[i] = True 
                backtracking(arr, path)
                path.pop()
                visited_index[i] = False
        backtracking(self.org_nums, [])
        
    def reset(self):
        """
        :rtype: List[int]
        """
        return self.org_nums

    def shuffle(self):
        """
        :rtype: List[int]
        """
        import random
        # print(self.shuffles)
        return random.choice(self.shuffles)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
