# https://labuladong.gitee.io/algo/4/30/100/

# 回溯算法其实就是我们常说的 DFS 算法，本质上就是一种暴力穷举算法。

# 解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：
# 1、路径：也就是已经做出的选择。
# 2、选择列表：也就是你当前可以做的选择。
# 3、结束条件：也就是到达决策树底层，无法再做选择的条件。


# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
    
#     for 选择 in 选择列表:
#         // 前序遍历需要的操作
#         #做选择
#         将该选择从选择列表移除
#         backtrack(路径, 选择列表)
#         // 后序遍历需要的操作
#         #撤销选择
#         将该选择再加入选择列表

# void traverse(TreeNode root) {
#     for (TreeNode child : root.childern)
#         // 前序遍历需要的操作
#         traverse(child);
#         // 后序遍历需要的操作
# }


# 其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」