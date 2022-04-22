badge_times = [
  ["Paul",     "1355"],
  ["Jennifer", "1910"],
  ["John",      "835"],
  ["John",      "830"],
  ["Paul",     "1315"],
  ["John",     "1615"],
  ["John",     "1640"],
  ["Paul",     "1405"],
  ["John",      "855"],
  ["John",      "930"],
  ["John",      "915"],
  ["John",      "730"],
  ["John",      "940"],
  ["Jennifer", "1335"],
  ["Jennifer",  "730"],
  ["John",     "1630"],
  ["Jennifer",    "5"]
]

# refer to LC1604
import collections
def getEmployeeBadgeThree(badge_times):
    dctName2Times = collections.defaultdict(list)
    for name, time in badge_times:
        new_time = '000' + time
        new_time = new_time[-4:]
        hour, minute = new_time[:2], new_time[2:]
        dctName2Times[name].append((int(hour)*60 + int(minute), time))
    
    res = collections.defaultdict(set)
    for name, lstTimes in dctName2Times.items():
        if len(lstTimes) <= 2:
            continue 
        lstTimes.sort(key = lambda x: x[0])
        # print(name, lstTimes)
        for i in range(len(lstTimes) - 2):
            if lstTimes[i+2][0] - lstTimes[i][0] <= 60:
                print(name, lstTimes[i][1], lstTimes[i+1][1], lstTimes[i+2][1])
                res[name].add(lstTimes[i][1])
                res[name].add(lstTimes[i+1][1])
                res[name].add(lstTimes[i+2][1])
    return [[name, sorted(list(setTimes))] for name, setTimes in res.items()]
print(getEmployeeBadgeThree(badge_times))
# Expected output (in any order)
#   John:  830  835  855  915  930
#   Paul: 1315 1355 1405



###############################################################
# follow up:  
badge_records = [
["Paul", "1214", "enter"],
["Paul", "830", "enter"],
["Curtis", "1100", "enter"],
["Paul", "903", "exit"],
["John", "908", "exit"],
["Paul", "1235", "exit"],
["Jennifer", "900", "exit"],
["Curtis", "1330", "exit"],
["John", "815", "enter"],
["Jennifer", "1217", "enter"],
["Curtis", "745", "enter"],
["John", "1230", "enter"],
["Jennifer", "800", "enter"],
["John", "1235", "exit"],
["Curtis", "810", "exit"],
["Jennifer", "1240", "exit"],
]
def getStr2Time(time):
    new_time = time
    new_time = '000' + time
    new_time = new_time[-4:]
    hour, minute = new_time[:2], new_time[2:]
    return hour * 60 + minute

def getLargestGroup(badge_records):
    dctStrTime2Time = {}
    for name, time, action in badge_records:
        dctStrTime2Time[time] = getStr2Time(time)
    badge_records.sort(key = lambda x: dctStrTime2Time[x[1]])
    print(badge_records)
    insideRoom = []
    name
    for name, time, action in badge_records:
        if action == 'enter':
            insideRoom.append(name)
    pass
# getLargestGroup(badge_records)
"""
第三题: Employee Badge Time
/*
We are working on a security system for a badged-access room in our company's building.
We want to find employees who badged into our secured room unusually often. We have an unordered 
list of names and entry times over a single day. Access times are given as numbers up to four digits 
in length using 24-hour time, such as "800" or "2250".
Write a function that finds anyone who badged into the room three or more times in a one-hour period. 
Your function should return each of the employees who fit that criteria, plus the times that they badged 
in during the one-hour period. If there are multiple one-hour periods where this was true for an employee, 
just return the first one.
badge_times = [
  ["Paul",     "1355"],
  ["Jennifer", "1910"],
  ["John",      "835"],
  ["John",      "830"],
  ["Paul",     "1315"],
  ["John",     "1615"],
  ["John",     "1640"],
  ["Paul",     "1405"],
  ["John",      "855"],
  ["John",      "930"],
  ["John",      "915"],
  ["John",      "730"],
  ["John",      "940"],
  ["Jennifer", "1335"],
  ["Jennifer",  "730"],
  ["John",     "1630"],
  ["Jennifer",    "5"]
]
Expected output (in any order)
  John:  830  835  855  915  930
  Paul: 1315 1355 1405
n: length of the badge records array
*/

第三题 FollowUp: Largest Group in Room
/*
We want to find employees who badged into our secured room together often. Given an unordered list of 
names and access times over a single day, find the largest group of people that were in the room together 
during two or more separate time periods, and the times when they were all present.
badge_records = [
["Paul", "1214", "enter"],
["Paul", "830", "enter"],
["Curtis", "1100", "enter"],
["Paul", "903", "exit"],
["John", "908", "exit"],
["Paul", "1235", "exit"],
["Jennifer", "900", "exit"],
["Curtis", "1330", "exit"],
["John", "815", "enter"],
["Jennifer", "1217", "enter"],
["Curtis", "745", "enter"],
["John", "1230", "enter"],
["Jennifer", "800", "enter"],
["John", "1235", "exit"],
["Curtis", "810", "exit"],
["Jennifer", "1240", "exit"],
]
Expected output:
John, Paul, Jennifer: 830 to 900, 1230 to 1235
For this input data:
From 830 til 900, the room contains Jennifer, John, and Paul.
From 1230 til 1235, the room contains Curtis, Paul, Jennifer, and John.
The group "Jennifer, John, Paul" exists at both of these times, and is the largest group that exists multiple times.
You should note that the group is a subset of the people in the room from 1230 to 1235
"""