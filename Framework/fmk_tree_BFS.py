# https://labuladong.gitee.io/algo/1/5/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 问题的本质就是让你在一幅「图」中找到从起点 start 到终点 target 的最近距离
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
    
# BFS 相对 DFS 的最主要的区别是：BFS 找到的路径一定是最短的，但代价就是空间复杂度可能比 DFS 大很多
# 假设给你的这个二叉树是满二叉树，节点数为 N，对于 DFS 算法来说，空间复杂度无非就是递归堆栈，最坏情况下顶多就是树的高度，也就是 O(logN)。
# 但是你想想 BFS 算法，队列中每次都会储存着二叉树一层的节点，这样的话最坏情况下空间复杂度应该是树的最底层节点的数量，也就是 N/2，用 Big O 表示的话也就是 O(N)。
# 由此观之，BFS 还是有代价的，一般来说在找最短路径的时候使用 BFS，其他时候还是 DFS 使用得多一些（主要是递归代码好写）。