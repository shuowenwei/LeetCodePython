# https://labuladong.gitee.io/algo/4/30/100/

# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return
    
#     for 选择 in 选择列表:
#         #做选择
#         将该选择从选择列表移除
#         backtrack(路径, 选择列表)
#         #撤销选择
#         将该选择再加入选择列表

# 其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」