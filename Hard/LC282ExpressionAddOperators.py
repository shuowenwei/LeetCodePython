# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/expression-add-operators/

solution: https://leetcode.com/problems/expression-add-operators/submissions/


"""
class Solution(object):
    # def __init__(self):
    #     self.answer = [] 
    #     self.nums = None
    #     self.target = None

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.nums = num
        self.target = target
        self.res = []
        self.recurse(0,0, [], 0)
        return self.res

    def recurse(self, index, value, ops, prev_val):
        nums = self.nums
        if index == len(nums):
            if value == self.target:
                self.res.append("".join(ops))
            return
        
        #this is the current operand, which is not necessarily a single digit 
        currVal = 0 
        for i in range(index, len(nums)):
            # starting from nums[index], compute current operand on the fly 
            currVal = currVal * 10 + int(nums[i]) 
            
            # If this is the first operand, we simple go onto the next recursion.
            if index == 0: 
                self.recurse(i+1, currVal, ops + [str(currVal)], currVal) # no 
            else:
                # when '*'
                v = value - prev_val
                self.recurse(i+1, v + (prev_val * currVal), ops + ['*' + str(currVal)], prev_val * currVal)
                # when "+" 
                self.recurse(i+1, value + currVal, ops + ['+' + str(currVal)], currVal)
                # when "-"
                self.recurse(i+1, value - currVal, ops + ['-' + str(currVal)], -currVal)
            # If a string starts with '0', then it has to be an operand on its own. We can't have '025' as an operand. That doesn't make sense
            if nums[index] == '0':
                break 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
            