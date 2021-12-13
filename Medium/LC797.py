# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/all-paths-from-source-to-target/

https://labuladong.gitee.io/algo/2/19/34/

https://labuladong.gitee.io/algo/2/19/35/

LC797, LC207, LC210

"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        import copy 
        res = []
        def traverse(graph, node, path):
            path.append(node)
            if node == len(graph)-1:
                res.append(copy.deepcopy(path))
                path.pop()
                return
            for v in graph[node]:
                traverse(graph, v, path)
            path.pop()
        traverse(graph, 0, [])
        return res
