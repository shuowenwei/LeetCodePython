# 前缀和数组 https://labuladong.gitee.io/algo/2/21/53/

# 差分数组 https://labuladong.gitee.io/algo/2/21/54/

class PrefixSum(object):
    # // 前缀和数组
    # /* 输入一个数组，构造前缀和 */
    def __init__(self, nums):
        n = len(nums) 
        self.preSum = [0]*(n+1)
        # // 计算 nums 的累加和
        # self.preSum[i] means sum(nums[0:i]), [0,...,i), not include nums[i]
        for i in range(1, n+1):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]
    
    # /* 查询闭区间 [i, j] 的累加和 */
    def sumRange(self, i, j):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[j+1] - self.preSum[i]



# // 差分数组工具类 
# LC370, LC1109, LC1094
class Difference(object):
    def __init__(self, nums):
        # // 差分数组
        assert len(nums) > 0, 'Error, empty array'
        n = len(nums) 
        self.diff = [0] * n
        self.diff[0] = nums[0]
        for i in range(1, n):
            self.diff[i] = nums[i] - nums[i - 1]
        
    # /* 给闭区间 [i,j] 增加 val（可以是负数）*/
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff): 
            self.diff[j+1] -= val
        # 当 j+1 >= diff.length 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 val 了。

    # /* 返回结果数组 */
    def result(self):
        res = [0] * len(self.diff)
        # // 根据差分数组构造结果数组
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res
