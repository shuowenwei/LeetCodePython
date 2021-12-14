# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/is-graph-bipartite/

https://labuladong.gitee.io/algo/2/19/36/

LC797, LC207, LC210
LC785, LC886

"""
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        ok = [True]
        visited = [False] * len(graph)
        color = [False] * len(graph)
        def traverse(graph, s):
            if ok[-1] is False:
                return 
            visited[s] = True
            for neighbor in graph[s]:
                if visited[neighbor] is False:
            # // 相邻节点 w 没有被访问过
            # // 那么应该给节点 w 涂上和节点 v 不同的颜色
                    color[neighbor] = not color[s]
                    traverse(graph, neighbor)
                else:
            # // 相邻节点 w 已经被访问过
            # // 根据 v 和 w 的颜色判断是否是二分图
                    if color[s] == color[neighbor]:
                    # // 若相同，则此图不是二分图
                        ok.append(False)
                        return 

        for i in range(len(graph)):
            if visited[i] is False:
                traverse(graph, i)
        return ok[-1]
