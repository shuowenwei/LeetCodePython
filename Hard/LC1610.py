# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/maximum-number-of-visible-points/

https://leetcode.com/problems/maximum-number-of-visible-points/discuss/894732/Python-C%2B%2B-3-Simple-Steps

"""
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        if angle >= 360:
            return len(points)
        from math import atan2
        points_polar_angles = []
        l1, l2 = location
        same_points_with_location = 0
        for x, y in points:
            if x == l1 and y == l2:
                same_points_with_location += 1
                continue
            alpha = atan2(y-l2, x-l1) * (180 / math.pi) # can't be zero 
            if alpha < 0:
                alpha += 360 
            points_polar_angles.append( alpha )
            
        points_polar_angles.sort()
        points_polar_angles = points_polar_angles + [a+360 for a in points_polar_angles]
        windonw = angle
        i, j = 0, 0
        res = 0 
        while j < len(points_polar_angles):
            while j < len(points_polar_angles) and points_polar_angles[j] - points_polar_angles[i] <= angle:
                j += 1
            res = max(res, j-i)
            while j < len(points_polar_angles) and points_polar_angles[j] - points_polar_angles[i] > angle:
                i += 1
        return res + same_points_with_location 
