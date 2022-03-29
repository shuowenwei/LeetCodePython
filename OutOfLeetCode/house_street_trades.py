# refer to: https://leetcode.com/discuss/interview-question/882324/robinhood-phone-screen

from collections import Counter

class TradesMatcher:
    def filter_matching_trades(self, tradesA, tradesB):
        """ 
        tradesA: List[str] 
        tradesB: List[str]
        return: List[str]
        """
        aCounter = Counter(tradesA)
        bCounter = Counter(tradesB)
        # Discard exact matches
        aCounter.subtract(bCounter)
        uniqueAs = +aCounter
        uniqueBs = -aCounter
        
        aTrades = sorted(uniqueAs.elements())
        bTrades = sorted(uniqueBs.elements())
        return self.discard_fuzzy_matches(aTrades, bTrades)

    def is_fuzzy_match(self, a, b):
        id_index = b.rfind(',')
        return a.startswith(b[:id_index])

    def discard_fuzzy_matches(self, aTrades, bTrades):
        res = []
        a_idx = b_idx = 0
        while a_idx < len(aTrades) and b_idx < len(bTrades):
            a = aTrades[a_idx]
            b = bTrades[b_idx]
            if self.is_fuzzy_match(a, b):
                a_idx += 1
                b_idx += 1
                continue
            if a < b:
                res.append(a)
                a_idx += 1
            else:
                res.append(b)
                b_idx += 1
                
        while a_idx < len(aTrades):
            res.append(aTrades[a_idx])
            a_idx += 1

        while b_idx < len(bTrades):
            res.append(bTrades[b_idx])
            b_idx += 1

        return res
