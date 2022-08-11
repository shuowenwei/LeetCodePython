# https://labuladong.gitee.io/algo/1/8/
# https://labuladong.gitee.io/algo/2/21/57/

# LC704, LC34, LC875, LC1101, LC410

# 分析二分查找的一个技巧是：不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节
# 对于寻找左右边界的二分搜索，常见的手法是使用左闭右开的「搜索区间」，我们还根据逻辑将「搜索区间」全都统一成了两端都闭，便于记忆，只要修改两处即可变化出三种写法：
def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1 
    while left <= right: # break when left == right + 1 
        mid = left + (right - left) / 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # // 直接返回
            return mid
    return -1 

def left_bound(nums, target):
    left = 0
    right = len(nums) - 1 
    while left <= right: # break when left == right + 1 
        mid = left + (right - left) / 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # // 别返回，锁定左侧边界
            right = mid - 1 
    # // 最后要检查 left 越界的情况
    if left > len(nums) - 1  or nums[left] != target: 
        return -1 
    return left 


def right_bound(nums, target):
    left = 0
    right = len(nums) - 1 
    while left <= right: # break when left == right + 1 
        mid = left + (right - left) / 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # // 别返回，锁定右侧边界
            left = mid + 1 
    # // 最后要检查 right 越界的情况
    if right < 0 or nums[right] != target:
        return -1 
    return right

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
