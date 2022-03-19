# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/asteroid-collision/

LC735, LC2126
"""
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # positive means moving right, negative means moving left
        stack = []
        for asteroid in asteroids:
            # safe to enter stack:
            # 1. when stack is empty
            # 2. when asteroid and stack[-1] both moving left (negative)
            # 3. when asteroid moving right (positive) (regardless of stack[-1])
            if len(stack) == 0 or asteroid * stack[-1] > 0 or asteroid > 0:
                stack.append(asteroid)
            # possible collision: asteroid moving left, stack[-1] moving right
            if asteroid < 0 and stack[-1] > 0:
                # keep popping stack
                while stack and abs(asteroid) > abs(stack[-1]) and stack[-1] > 0:
                    stack.pop()
                # cancel out
                if stack and asteroid + (stack[-1]) == 0:
                    stack.pop()
                # empty stack or same direction
                elif len(stack) == 0 or asteroid * stack[-1] > 0:
                    stack.append(asteroid)
        return stack
        