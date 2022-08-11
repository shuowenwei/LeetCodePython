# https://labuladong.gitee.io/algo/2/21/58/
# LC704, LC34, LC875, LC1101, LC410

# 二分搜索问题的泛化
# 什么问题可以运用二分搜索算法技巧？
# 首先，你要从题目中抽象出一个自变量 x，一个关于 x 的函数 f(x)，以及一个目标值 target。
# 同时，x, f(x), target 还要满足以下条件：
# 1、f(x) 必须是在 x 上的单调函数（单调增单调减都可以）。
# 2、题目是让你计算满足约束条件 f(x) == target 时的 x 的值。

def f(nums, x):
    return nums[x] 

def solution(nums, target):
    if len(nums) == 0: return -1
    
    # // 问自己：自变量 x 的最小值是多少？
    left = ... 
    # // 问自己：自变量 x 的最大值是多少？
    right = ... + 1
    while left < right: 
        mid = left + (right - left)/2
        if f(mid) == target:
            # // 问自己：题目是求左边界还是右边界？
            # // ...
            pass
        elif f(mid) < target:
            # // 问自己：怎么让 f(x) 大一点？
            # // ...
            pass
        elif f(mid) > target:
            # // 问自己：怎么让 f(x) 小一点？
            # // ...
            pass 
    return left