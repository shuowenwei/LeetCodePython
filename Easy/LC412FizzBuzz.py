# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/fizz-buzz/
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [('Fizz' if i % 3 == 0 else '') +
                ('Buzz' if i % 5 == 0 else '') + 
                (str(i) if not (i % 3 == 0 or i % 5 == 0) else '') 
                for i in range(1, n+1) ]
    """ 
        res = []
        for i in range(1,n+1):
            if i % 15 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res 
        
    """