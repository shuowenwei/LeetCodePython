prereqs_courses1 = [
["Foundations of Computer Science", "Operating Systems"],
["Data Structures", "Algorithms"],
["Computer Networks", "Computer Architecture"],
["Algorithms", "Foundations of Computer Science"],
["Computer Architecture", "Data Structures"],
["Software Design", "Computer Networks"]
]

prereqs_courses2 = [
      ["Data Structures", "Algorithms"],
      ["Algorithms", "Foundations of Computer Science"],
      ["Foundations of Computer Science", "Logic"]
  ]
import collections

def courseSchedule(prereqs_course):
    all_courses = set()
    indegree = collections.defaultdict(int)
    graph = collections.defaultdict(set)
    for takeFirst, thenCanTake in prereqs_course:
        all_courses.add(takeFirst)
        all_courses.add(thenCanTake)
        graph[takeFirst].add(thenCanTake)
        indegree[thenCanTake] += 1
        
    count = 0 
    starters = [c for c in all_courses if indegree[c] == 0]
    q = collections.deque(starters)
    course_order = []
    while q:
        cur = q.popleft()
        count += 1
        course_order.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)       
    if len(course_order) % 2 == 0:
        mid = len(course_order) // 2 - 1
    else:
        mid = len(course_order) // 2
    return course_order[mid]
# print(courseSchedule(prereqs_courses1))
# print(courseSchedule(prereqs_courses2))



all_courses_1 = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Graphics", "Networking"],
    ["Networking", "Algorithms"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]
all_courses_2 = [
    ["Course_3", "Course_7"],
    ["Course_0", "Course_1"],
    ["Course_1", "Course_2"],
    ["Course_2", "Course_3"],
    ["Course_3", "Course_4"],
    ["Course_4", "Course_5"],
    ["Course_5", "Course_6"],
]
def courseScheduleAllPath(prereqs_course):
    all_courses = set()
    indegree = collections.defaultdict(int)
    graph = collections.defaultdict(set)
    for takeFirst, thenCanTake in prereqs_course:
        all_courses.add(takeFirst)
        all_courses.add(thenCanTake)
        graph[takeFirst].add(thenCanTake)
        indegree[thenCanTake] += 1

    all_path = []
    starters = [c for c in all_courses if indegree[c] == 0]
    # print('starters', starters)
    def backtracking(node, path, tmpGraph, tmpIndegree):
        if len(tmpGraph[node]) == 0:
            all_path.append(path[:])
            return
        for nxt_node in tmpGraph[node]:
            path.append(nxt_node)
            tmpIndegree[nxt_node] -= 1
            onPath[nxt_node] = True 
            backtracking(nxt_node, path, tmpGraph, tmpIndegree)
            path.pop()
            tmpIndegree[nxt_node] += 1
            onPath[nxt_node] = False

    for start in starters:
        onPath = {c:False for c in all_courses}
        tmpGraph = graph
        tmpIndegree = indegree
        backtracking(start, [start], tmpGraph, tmpIndegree)

    # print('all_path', len(all_path), all_path)
    res = []
    for path in all_path:
        if len(path) % 2 == 0:
            mid = len(path) // 2 - 1
        else:
            mid = len(path) // 2
        res.append(path[mid])
    return list(set(res))

print(courseScheduleAllPath(all_courses_1))
print(courseScheduleAllPath(all_courses_2))
    
"""
第一题：Course Schedule Mid
Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite.
There is only one path through the program.
Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student 
will be taking when they are halfway through their program. (If a track has an even number of courses, and therefore has 
two "middle" courses, you should return the first one.)
  Sample input 1: (arbitrarily ordered)
  const prereqs_courses1 = [
      ["Foundations of Computer Science", "Operating Systems"],
      ["Data Structures", "Algorithms"],
      ["Computer Networks", "Computer Architecture"],
      ["Algorithms", "Foundations of Computer Science"],
      ["Computer Architecture", "Data Structures"],
      ["Software Design", "Computer Networks"]
  ]
  In this case, the order of the courses in the program is:
      Software Design
      Computer Networks
      Computer Architecture
      Data Structures
      Algorithms
      Foundations of Computer Science
      Operating Systems
  Sample output 1:
      "Data Structures"
  Sample input 2:
  prereqs_courses2 = [
      ["Data Structures", "Algorithms"],
      ["Algorithms", "Foundations of Computer Science"],
      ["Foundations of Computer Science", "Logic"]
  ]
  Sample output 2:
      "Algorithms"
  Sample input 3:
  prereqs_courses3 = [
      ["Data Structures", "Algorithms"],
  ]
  Sample output 3:
      "Data Structures"
  Complexity analysis variables:
  n: number of pairs in the input

第一题 FollowUp: Course Schedule (多个Path)
/*
Students may decide to take different "tracks" or sequences of courses in the Computer Science curriculum. 
There may be more than one track that includes the same course, but each student follows a single linear 
track from a "root" node to a "leaf" node. In the graph below, their path always moves left to right.
Write a function that takes a list of (source, destination) pairs, and returns the name of all of the courses 
that the students could be taking when they are halfway through their track of courses.
Sample input 1:
all_courses_1 = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Graphics", "Networking"],
    ["Networking", "Algorithms"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]
Sample output 1 (in any order):
          ["Data Structures", "Networking", "Creative Writing", "Databases"]
All paths through the curriculum (midpoint *highlighted*):
Intro to C.S. -> Graphics -> *Networking* -> Algorithms -> Cobol
Intro to C.S. -> *Data Structures* -> Algorithms -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> Compiler
Creative Writing -> *Databases* -> System Administration
*Creative Writing* -> System Administration
Creative Writing -> *Data Structures* -> Algorithms -> COBOL
Creative Writing -> *Data Structures* -> Logic -> COBOL
Creative Writing -> *Data Structures* -> Logic -> Compilers

Sample input 2:
all_courses_2 = [
    ["Course_3", "Course_7"],
    ["Course_0", "Course_1"],
    ["Course_1", "Course_2"],
    ["Course_2", "Course_3"],
    ["Course_3", "Course_4"],
    ["Course_4", "Course_5"],
    ["Course_5", "Course_6"],
]
Sample output 2 (in any order):
["Course_2", "Course_3"]
Complexity analysis variables:
n: number of pairs in the input
"""