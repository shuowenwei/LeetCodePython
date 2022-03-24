# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

"""
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        edge = 1
         # // 任何时候，边数都不能小于 0
        for node in preorder.split(','):
            # // 空指针消耗一条空闲边
            if node == '#':
                edge -= 1
                if edge < 0:
                    return False
            else:
                # // 非空节点消耗一条空闲边，增加两条空闲边
                edge -= 1
                if edge < 0:
                    return False
                edge += 2
        return edge == 0 # // 最后不应该存在空闲边


        # soluition 2: deserialize the tree 
        preorder = preorder.split(',') # convert to a list of vals 
        def deserialize(preorder):
            if len(preorder) == 0:
                return False
            # /****** 前序遍历位置 ******/
            # // 列表最左侧就是根节点
            rootVal = preorder.pop(0)
            if rootVal == '#':
                return True 
            return deserialize(preorder) and deserialize(preorder)
        return deserialize(preorder) and len(preorder) == 0