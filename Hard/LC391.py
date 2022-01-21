# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/perfect-rectangle/

https://labuladong.gitee.io/algo/4/32/139/
# 想判断最终形成的图形是否是完美矩形，需要从「面积」和「顶点」两个角度来处理。
# 当某一个点同时是 2 个或者 4 个小矩形的顶点时，该点最终不是顶点；当某一个点同时是 1 个或者 3 个小矩形的顶点时，该点最终是一个顶点。
# 2 和 4 都是偶数，1 和 3 都是奇数，我们想计算最终形成的图形中有几个顶点，也就是要筛选出那些出现了奇数次的顶点
LC391
"""
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if len(rectangles) == 0:
            return True
        min_left_point = [10**5, 10**5]
        max_right_point = [-10**5, -10**5]
        total_area = 0
        points = set()
        for x1, y1, x2, y2 in rectangles:
            rctg_area = (x2-x1)*(y2-y1)
            total_area += rctg_area
            # print(rctg_area)
            min_left_point[0] = min(min_left_point[0], x1)
            min_left_point[1] = min(min_left_point[1], y1)
            max_right_point[0] = max(max_right_point[0], x2)
            max_right_point[1] = max(max_right_point[1], y2)
            # vertices
            p1 = (x1, y1)
            p2 = (x1, y2)
            p3 = (x2, y1)
            p4 = (x2, y2)
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
                
        expect_area = (max_right_point[0]-min_left_point[0])*(max_right_point[1]-min_left_point[1])
        if total_area != expect_area or len(points) != 4: 
            return False
        bottomLeft = (min_left_point[0], min_left_point[1])
        topRight = (max_right_point[0], max_right_point[1])
        if bottomLeft not in points or topRight not in points:
            return False
        return True
