# https://labuladong.gitee.io/algo/1/8/

# 分析二分查找的一个技巧是：不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1 
    mid = (left + right) / 2 
    while left <= right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
            mid = (left + right) / 2 
        elif nums[mid] > target:
            right = mid - 1
            mid = (left + right) / 2  
    return -1 

# 搜索一个元素时，搜索区间两端闭。
# while条件带等号，否则需要打补丁。
# if相等就返回，其他的事情甭操心。
# mid必须加减一，因为区间两端闭。
# while结束就凉了，凄凄惨惨返回-1。

# 搜索左右边界时，搜索区间要阐明。
# 左闭右开最常见，其余逻辑便自明。
# while要用小于号，这样才能不漏掉。
# if相等别返回，利用mid锁边界。
# mid加一或减一？要看区间开或闭。
# while结束不算完，因为你还没返回。
# 索引可能出边界，if检查保平安。
