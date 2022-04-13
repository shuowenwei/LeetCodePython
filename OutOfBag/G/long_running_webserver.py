"""
refer to https://leetcode.com/discuss/interview-question/1533097/Google-Onsite-L4/1123677

A long running webserver is writing to a log file, one request summary per line. 
Here is an example file: 

# timestamp(millis), URL, status, processing time
1000001, /index.html, 200, 150 
1000002, /article/1234.html, 500, 1 
1000005, /index.html, 200, 50 
1001000, /article/4321.html, 200, 10

Return all the input timestamp but associated with the number of requests being processed at the time of the timestamp.

Output :
1000001 --> 1
1000002 --> 2  (since the first process is still running, timestamp 1000002 would have two processes running)
1000005 --> 2  (since the first process is still running, timestamp 1000005 would have two processes running)
1001000 --> 1

similiar to LC1834
"""

from heapq import heappush, heappop
def numProcessPerTimestamp(time_url_status_time):
    hp = []
    res = {}
    timestamps = []
    time_url_status_time.sort(key = lambda x: x[0])
    
    for timestamp, url, status, time in time_url_status_time:
        timestamps.append(timestamp)
        res[timestamp] = 1
        while hp:
            if timestamp <= hp[0]:
                res[timestamp] = len(hp) + 1 
                break
            else:
                heappop(hp)
        heappush(hp, timestamp + time)
    return res 

time_url_status_time = [[1000001, '/index.html', 200, 150],
                        [1000002, '/article/1234.html', 500, 1],
                        [1000005, '/index.html', 200, 50],
                        [1001000, '/article/4321.html', 200, 10]]

r = numProcessPerTimestamp(time_url_status_time)
print(r)