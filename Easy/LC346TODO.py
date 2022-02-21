# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/moving-average-from-data-stream/

https://goodtecher.com/leetcode-346-moving-average-from-data-stream/

Time Complexity: O(N)
Space Complexity: O(N)
"""
class MovingAverage:
    
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.numbers = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.numbers.append(val)
        
        if len(self.numbers) > self.size:
            return sum(self.numbers[-(self.size):]) / self.size 
                
        return sum(self.numbers) / len(self.numbers) 
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

