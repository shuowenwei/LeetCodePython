# refer to https://leetcode.com/discuss/interview-question/1052406/robinhood-telephonic-interviewreject
"""
Given a stream of incoming "buy" and "sell" orders (as lists of limit price, quantity, and side, like
["155", "3", "buy"]), determine the total quantity (or number of "shares") executed.

A "buy" order can be executed if there is a corresponding "sell" order with a price that is less than or
equal to the price of the "buy" order.
Similarly, a "sell" order can be executed if there is a corresponding "buy" order with a price that is
greater than or equal to the price of the "sell" order.
It is possible that an order does not execute immediately if it isn't paired to a counterparty. In that 
case, you should keep track of that order and execute it at a later time when a pairing order is found.

You should ensure that orders are filled immediately at the best possible price. That is, an order 
should be executed when it is processed, if possible. Further, "buy" orders should execute at the 
lowest possible price and "sell" orders at the highest possible price at the time the order is handled.

Note that orders can be partially executed.

sell 3
sell 2
sell 1 
--------
buy 3
buy 2
buy 1
"""

import heapq
def returnExceutedShares(orders):
    buyMaxHeap, sellMinHeap = [], []
    executedShares = 0
    for price, shares, orderType in orders: # Time O(NlogN)
        price, shares = int(price), int(shares)
        initShares = shares
        
        if orderType == 'buy':
            while shares > 0 and len(sellMinHeap) > 0:
                minSellPrice, minSellShares = sellMinHeap[0]
                if minSellPrice <= price:
                    # Check if the sell shares less than or equal to price
                    heapq.heappop(sellMinHeap)
                    if shares < minSellShares:
                        # Execute all shares and re push remainders into sellMinHeap
                        heapq.heappush(sellMinHeap, (minSellPrice, minSellShares - shares))
                        shares = 0
                    else:
                        # Execute minSellShares
                        shares -= minSellShares
                else:
                    # If not, break
                    break
            if shares > 0:
                heapq.heappush(buyMaxHeap, (-price, shares))
        else: # orderType == 'sell':
            while shares > 0 and len(buyMaxHeap) > 0:
                maxBuyPrice, maxBuyShares = -buyMaxHeap[0][0], buyMaxHeap[0][1]
                if maxBuyPrice >= price:
                    # Check if the buy shares greater than or equal to price
                    heapq.heappop(buyMaxHeap)
                    if shares < maxBuyShares:
                        # Execute all shares and re push remainders into buyMaxHeap
                        heapq.heappush(buyMaxHeap, (-maxBuyPrice, maxBuyShares - shares))
                        shares = 0
                    else:
                        # Execute maxBuyShares
                        shares -= maxBuyShares
                else:
                    break
            if shares > 0:
                heapq.heappush(sellMinHeap, (price, shares))
        executedShares += (initShares - shares)
    return executedShares

if __name__ == '__main__':
    assert returnExceutedShares([
        ['150', '5', 'buy'],    # Order A
        ['190', '1', 'sell'],   # Order B
        ['200', '1', 'sell'],   # Order C
        ['100', '9', 'buy'],    # Order D
        ['140', '8', 'sell'],   # Order E
        ['210', '4', 'buy'],    # Order F
    ]) == 9

orders = [
        ['150', '5', 'buy'],    # Order A
        ['190', '1', 'sell'],   # Order B
        ['200', '1', 'sell'],   # Order C
        ['100', '9', 'buy'],    # Order D
        ['140', '8', 'sell'],   # Order E
        ['210', '4', 'buy'],    # Order F
    ]
print(returnExceutedShares(orders))