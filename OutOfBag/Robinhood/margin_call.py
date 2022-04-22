"""
https://leetcode.com/discuss/interview-question/882324/robinhood-phone-screen

depends they ask questions regarding to trading for onsite:
input will be a list of trades, as of timestamp, symbol, B/S, quantity, price
[["2", "NVDA", "B", "10", "10"],
["3", "GOOG", "B", "20", "5"],
["10", "NVDA", "S", "5", "15"]]

consolidate the orders
[["CASH", "875"],
["NVDA", "5"],
["GOOG", "20"]]

and then do a margin call , anytime you hit a negative cash balance you sell trades 
until cash is positive and then continue with the next trades.

refer to: https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=825477&ctid=232523

股票交易的log，包括 timestamp, name, quantity, price，初始cash是1000刀，
第一问要求print out最终剩下的cash和股票的数量，不考虑cash不够的情况。
第二问要考虑marginal call的情况，就是如果cash不够直接买入，强制卖出现有的股价最高的股票，直到有足够的cash。
如果有同一个股票有多个价格，按最近的价格计算。

"""

logs = [["2", "NVDA", "B", "10", "10"],
["3", "GOOG", "B", "20", "5"],
["10", "NVDA", "S", "5", "15"],
["13", "GOOG", "B", "50", "20"],
]
import collections
import math
from heapq import heappop, heappush
def getMarginCall(logs, cash = 1000):
    logs = [[float(time), symbol, action, float(quantity), float(price)] for time, symbol, action, quantity, price in logs]
    logs.sort(key = lambda x: x[0])
    res = {'cash': cash}
    dctSymbol2Price = collections.defaultdict(float)
    hp_bought = []
    for time, symbol, action, quantity, price in logs:
        dctSymbol2Price[symbol] = price # overwrite with latest price
        if action == 'S':
            cash = cash + quantity * price
            res[symbol] -= quantity
            heappush(hp_bought, [-price, symbol])

        if action == 'B':
            cash = cash - quantity * price
            if symbol not in res:
                res[symbol] = quantity
            else: 
                res[symbol] += quantity
                
            while cash < 0:
                price, symbol = heappop(hp_bought)
                # highest_price = -price
                if res[symbol] * dctSymbol2Price[symbol] + cash > 0:
                    minUnits = math.ceil(float(-cash) / dctSymbol2Price[symbol])
                    res[symbol] -= minUnits
                    cash += minUnits * dctSymbol2Price[symbol]
                    heappush(hp_bought, [-dctSymbol2Price[symbol], symbol])
                else:
                    cash += res[symbol] * dctSymbol2Price[symbol]
            
            heappush(hp_bought, [-price, symbol])
                
        res['cash'] = cash
        print(time, '--->', res)
        
    return res
print(getMarginCall(logs)) 