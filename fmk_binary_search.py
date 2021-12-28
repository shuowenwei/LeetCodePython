# https://labuladong.gitee.io/algo/1/8/
# https://labuladong.gitee.io/algo/2/21/57/

# LC704, LC34, LC875, LC1101, LC410

# 分析二分查找的一个技巧是：不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节
# 对于寻找左右边界的二分搜索，常见的手法是使用左闭右开的「搜索区间」，我们还根据逻辑将「搜索区间」全都统一成了两端都闭，便于记忆，只要修改两处即可变化出三种写法：
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1 
    while left <= right: # break when left == right + 1 
        mid = (left + right) / 2 
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1 

def left_bound(nums, target):
    left = 0
    right = len(nums) - 1 
    while left <= right: # break when left == right + 1 
        mid = (left + right) / 2 
        if nums[mid] == target:
            right = mid - 1 
        elif nums[mid] < target:
            left = mid + 1 
        elif nums[mid] > target:
            right = mid - 1
    if left > len(nums) - 1  or nums[left] != target: 
        return -1 
    return left 


def right_bound(nums, target):
    left = 0
    right = len(nums) - 1 
    while left <= right: # break when left == right + 1 
        mid = (left + right) / 2 
        if nums[mid] == target:
            left = mid + 1 
        elif nums[mid] < target:
            left = mid + 1 
        elif nums[mid] > target:
            right = mid - 1
    if right < 0 or nums[right] != target:
        return -1 
    return right


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

# 第一个，最基本的二分查找算法：
# 因为我们初始化 right = nums.length - 1
# 所以决定了我们的「搜索区间」是 [left, right]
# 所以决定了 while (left <= right)
# 同时也决定了 left = mid+1 和 right = mid-1
# 因为我们只需找到一个 target 的索引即可
# 所以当 nums[mid] == target 时可以立即返回

# 第二个，寻找左侧边界的二分查找：
# 因为我们初始化 right = nums.length
# 所以决定了我们的「搜索区间」是 [left, right)
# 所以决定了 while (left < right)
# 同时也决定了 left = mid + 1 和 right = mid
# 因为我们需找到 target 的最左侧索引
# 所以当 nums[mid] == target 时不要立即返回
# 而要收紧右侧边界以锁定左侧边界

# 第三个，寻找右侧边界的二分查找：
# 因为我们初始化 right = nums.length
# 所以决定了我们的「搜索区间」是 [left, right)
# 所以决定了 while (left < right)
# 同时也决定了 left = mid + 1 和 right = mid
# 因为我们需找到 target 的最右侧索引
# 所以当 nums[mid] == target 时不要立即返回
# 而要收紧左侧边界以锁定右侧边界
# 又因为收紧左侧边界时必须 left = mid + 1
# 所以最后无论返回 left 还是 right，必须减一
