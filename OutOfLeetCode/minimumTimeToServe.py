# https://www.1point3acres.com/bbs/thread-855045-1-1.html
# n个服务员，m个人等位，给了数组里面元素是每个服务员服务一个人的时间，m>>n，当多个服务员空闲时候，
# 编号最小的去服务，问当你是第m+1个人的时候要等多久

# LC1071, LC2015, LC1834
from heapq import heappush, heappop
def getWaitingTime(nums, m):
    hp = []
    n = len(nums)
    for index, time in enumerate(nums):
        heappush(hp, (time, index))
    if m <= len(nums):
        return 0
    cur_time = 0
    perpoleServed = n
    while perpoleServed < m + 1:
        cur_time, i = heappop(hp)
        next_available_time = cur_time + nums[i]
        perpoleServed += 1
        heappush(hp, (next_available_time , i))
    return cur_time

nums = [2,3,5,7,9]
m = 100000
print('emma...', getWaitingTime(nums, m))
 
# class Solution(object):
#     def getOrder(self, tasks):
        # tasks_index = [(t[0], t[1], index) for index, t in enumerate(tasks)]
        # tasks_index.sort(key = lambda x: x[0])
        # from heapq import heappush, heappop
        # res = []
        # hp = []
        # pointer = 0 
        # cur_time = tasks_index[pointer][0] # earliest task to enter queue 
        # while len(res) < len(tasks_index): # break when all tasks are processed 
        #     # push all tasks with enter_time <= cur_time, when picking the shortest on to start
        #     while pointer < len(tasks_index) and cur_time >= tasks_index[pointer][0]:
        #         enter, processtime, index = tasks_index[pointer]
        #         heappush(hp, (processtime, index))
        #         pointer += 1
        #     if hp:
        #         processtime, index = heappop(hp)
        #         cur_time += processtime
        #         res.append(index)
        #     elif pointer < len(tasks_index):
        #         cur_time = tasks_index[pointer][0]
        # return res 
        
# https://www.1point3acres.com/bbs/thread-856372-1-1.html
def minimumTimeToServe(time, m):
    left = 1
    right = min(time) * m 
    def getTotalServed(time, waiting_time):
        res = 0
        for t in time:
            res += waiting_time / t
        return res

    while left < right:
        mid = left + (right - left) // 2
        totalServed = getTotalServed(time, mid)
        if totalServed >= m:
            right = mid 
        elif totalServed < m:
            left = mid + 1
    return left

time = [2,3,5,7,9]
m = 100000
print(minimumTimeToServe(time, m))
# def minimumTimeToServe(time, m): {
#   int l = 1, r = min(time) * m;
#   while (l < r) {
#     int mid = l + (r - l) / 2;
#     int totalServed = 0;
#     for (int t: time) {
#       totalServed += mid / t;
#     }
#     if (totalServed >= m) {
#       r = mid;
#     } else {
#       l = mid + 1;
#     }
#   }
#   return l;
# }