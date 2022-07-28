# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/course-schedule-iii/

https://leetcode.com/problems/course-schedule-iii/discuss/104847/Python-Straightforward-with-Explanation

LC1834, LC630
greedy
LC207, LC210, LC630
"""
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        hp = []
        start = 0 
        courses.sort(key = lambda x: x[1]) # Sort all the courses by their ending time
        for duration, endTime in courses:
            start += duration
            heappush(hp, -duration) # max heap 
            while start > endTime: # if is also fine, because each time we only need to remove at most one element from the pq
                #keep removing the longest duration course until they all end before endTime
                longestDurationCourse = - heappop(hp)
                start -= longestDurationCourse
        return len(hp)