# //  https://labuladong.gitee.io/algo/1/7/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
# // 岛屿系列题目的核心考点就是用 DFS/BFS 算法遍历二维数组。
# // 因为二维矩阵本质上是一幅「图」，所以遍历的过程中需要一个 visited 布尔数组防止走回头路

# // 二叉树遍历框架
def traverse(root: TreeNode):
    traverse(root.left)
    traverse(root.right)

# // 二维矩阵遍历框架
# void dfs(int[][] grid, int i, int j, boolean[] visited) {
def dfs(grid, i, j, visited):
    m, n = len(grid), len(grid[0]) 

    if i < 0 or j < 0 or i >= m or j >= n:
        # // 超出索引边界
        return    
    if (visited[i][j]):
        # // 已遍历过 (i, j)
        return

    # // 进入节点 (i, j)
    visited[i][j] = True 
    dfs(grid, i - 1, j) # // 上
    dfs(grid, i + 1, j) # // 下
    dfs(grid, i, j - 1) # // 左
    dfs(grid, i, j + 1) # // 右
