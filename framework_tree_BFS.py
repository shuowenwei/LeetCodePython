# https://labuladong.gitee.io/algo/1/5/

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# // 计算从起点 start 到终点 target 的最近距离
from collections import deque 
def BFS(start: TreeNode, target:TreeNode):
    q = deque() # // 核心数据结构
    visited = set() # // 避免走回头路
    
    q.append(start) # // 将起点加入队列
    visited.add(start) 
    step = 0 # // 记录扩散的步数

    while len(q) > 0:
        sz = len(q)
        # /* 将当前队列中的所有节点向四周扩散 */
        for i in range(len(q)):
            cur = q.popleft()
            # /* 划重点：这里判断是否到达终点 */
            if cur is target:
                return step 
            # /* 将 cur 的相邻节点加入队列 */
            for x in [cur.left, cur.right]: # cur.adj() 泛指 cur 相邻的节点，比如说二维数组中，cur 上下左右四面的位置就是相邻节点；
                if x not in visited:
                    q.append(x)
                    visited.add(x)
        # /* 划重点：更新步数在这里 */
        step += 1