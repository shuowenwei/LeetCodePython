/**
 * Given a log of website requests, where each line contains an entry with the following fields 
 (time, customerId, pageVisited), write an algorithm to find the top 3-page sequence of page 
 visits for all customers. Each line represents a request (A-Z) made by customer 
 (C#) at time T to one of the website's pages.

For example, given the following log file containing:

T0,C1,A
T0,C2,E
T1,C1,B
T1,C2,B
T2,C1,C
T2,C2,C
T3,C1,D
T3,C2,D
T4,C1,E
T5,C2,A

Sequence of visits for each customer: 

C1 = A -> B -> C -> D -> E

C2 = E -> B -> C -> D -> A

Answer: We see that the most common 3-page sequence visited by a customer is:  B->C->D
 * 
 * 
 * /
 
from collections import defaulltdict
 
def findMostCommonKPage(logs, k = 3):
    
    dctCustom2Pages = defaulltdict(list)
    dctKPage2Count = defaulltdict(int)
    # assuming it's sorted by time, otherwise: O(nlohn)
    maxVisits = 0 
    maxKPage = ''
    assert len(log.split()) == 3, ''
    for time, customerId, pageVisited in logs:
        
        
        dctCustom2Pages[customerId].append(pageVisited)
        
        if len(dctCustom2Pages[customerId]) >= k:
            KPageKey = '->'.join(dctCustom2Pages[customerId][:-k]) # "B->C->D"
            dctKPage2Count[KPageKey] += 1 
            if dctKPage2Count[KPageKey] >= maxVisits: # if last most visted 
                maxVisits = dctKPage2Count[KPageKey]
                maxKPage = KPageKey # listMaxKPage.append)() 
                
    return maxKPage, maxVisits
            

C1 = A -> B ( less than k)

C2 = E -> B -> C -> D -> A

C2 = E -> B -> B -> B -> A ? Q: "B->B->B"

'ECD'
    
    "T0,C1,A"
    "T0,C1,D"
    
    "T0,C1,D,A"
    
import unitest
class UnitTest_findMostCommonKPage(unitest.TestCase):
    logs = [
    T0,C1,A
    T0,C2,E
    T1,C1,B
    T1,C2,B
    T2,C1,C
    T2,C2,C
    T3,C1,D
    T3,C2,D
    T4,C1,E
    T5,C2,A
    ]
    
    k = 3 
    maxKPage, maxVisits = findMostCommonKPage(logs, k = 3)