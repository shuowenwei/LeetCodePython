# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/keys-and-rooms/

"""
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        entered = [False]*len(rooms)
        entered[0] = True
        stack = [0]
        while len(stack) > 0 : 
            openRoom = stack.pop()
            for k in rooms[openRoom]:
                if not entered[k]:
                    entered[k] = True
                    stack.append(k)
        return entered.count(True) == len(rooms)