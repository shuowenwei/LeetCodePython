# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/concatenated-words/

https://leetcode.com/problems/concatenated-words/discuss/836924/Python-Template-Word-Break-I-Word-Break-II-Concatenated-Words

LC139, LC140, LC472
- backtrack
"""
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # code form LC139
        def wordBreak(s, wordDict):
            dp = [False] * (len(s) + 1)
            dp[0] = True
            # dict_word = set(wordDict)
            for i in range(len(s)+1):
                for j in range(i):
                    if dp[j] and s[j:i] in wordDict:
                        dp[i] = -1
            return dp[-1]
        
        res = []
        if len(words) < 2:
            return res
        words.sort(key = lambda x:len(x)) #print(words)
        shorter_words = set()
        for w in words:
            if wordBreak(w, shorter_words):
                res.append(w)
            shorter_words.add(w)
        return res 
    
    
a = ["","ta","ye","mf","ge","br","lq","ax","yw","rv","av","os","np","tp","po","dc","wr","vl","sc","fq","su","eo","ua","kk","cw","aa","ly","fg","nx","ww","ss","wd","fd","cr","qe","qm","lt","tg","qa","oa","ku","at","yu","ng","re","vg","gu","yy","bc","ife","lfz","qtg","wsx","ryp","fso","had","lhv","nkq","svo","hwc","lmq","mat","kmm","sox","loc","ggk","hyw","cfq","lxu","hfl","cre","lmu","lmg","twn","kng","sid","vep","mwo","kbu","pey","lqs","gfve","qfpd","tpvo","gama","qxru","ppvs","akdt","dtlg","fecd","potn","koat","pybf","cvet","vruh","ahmv","tlnc","tyff","uwkl","wrxw","bilt","nxbk","coqs","pknt","tmnm","bcxw","eaum","fump","saeq","xbuw","uoay","hghv","wcbm","khhqr","xdnnl","qghoy","kdohe","rqdll","mumbh","mqrbq","xhflc","rlaks","wnnbq","agylw","rdrls","fdnor","yyhga","wljmg","onlvy","ffjfb","soqlh","gadgt","cpdxf","rwuvd","pfgsp","apsbu","nlwpw","vhfsf","caybc","npbep","ngzdc","walsx","ykbcn","wqrom","dhthp","eyelg","kfykd","pbdrx","rqyex","smkln","rfuyp","xbspa","wruqc","tgygdt","nhcvpf","vuzygv","ocedkt","xucubv","repgcx","mwrvel","egdgye","vkmxys","kqlima","mdtrgv","vomtuy","yxfeoh","rrklkb","cymbrl","htknfa","wpccoa","bwsezd","ueolqk","ordxzm","krvnaf","nxqmxr","dmoerc","eocfru","qevdyd","armuwp","opvrnx","ugrloq","hbsfyfv","bkkxcvg","nberblt","pbcnmhf","llkmagl","qnebmfl","xbhkkfg","iddymnl","udvmara","flhyfac","aysulvk","dqhqats","wygsnxk","myctacn","qfzwuwe","erpbaxq","wlrwyuy","hrtbfnq","yoifoyg","byyvhgh","kedhvwy","rhymsno","ocbbwwd","ubheeqt","mvndmua","wqqatye","nxlbkak","tovdtkr","brdeumb","tccvslp","npsoqsw","ckorgrm","gtghfxf","adoshnx","lehdfnr","tfsrptug","gttxwpuk","hdkbdxqg","ukmcowoe","reqqzzpw","yaqgault","cypqodxr","hnegtuxx","wtsbhgkd","xwdbycdu","suhesetv","gbndakaq","dphbfaal","pgowefka","nraoenhd","rkbdlchs","pxnktxkm","ngrwqpoh","eruffmlg","bxzovyew","rmbxlcmn","oncggqvr","dnrrgmem","wuznnlyd","syxngevs","yjyssbsoc","qmmidmvkn","glafbwzdd","fctkqlroq","gqgsomonv","ogwilaswn","xwnbcuggl","bhhlovgcx","nxtsnason","dccamymhp","hyfrdngjf","naefganqo","mtkewbprs","oxpmplpcg","uztnpqhdl","fkyvqguqq","feclhbvfuk","omwufbdfxu","ilebxwbcto","monmwvytby","gsfomhvpmy","rlbskqgfvn","uzvgyeette","phouoyhvls","odknlbvxrs","mabkapuoud","fkglorkkvx","rrbhfwohfv","rglnpxfqwu","afumtqugec","hdykehkefp","wtelvsqrru","bhqultkyfq","advraqovan","urbrmmadea","xmywegmtuno","nwedtubynsb","lfvobeyolyy","eouxbldsxzm","fgxnuohrnhg","qcagsyqggcf","gcdqbcdwbwa","lfnrhgsxkhx","akyprzzphew","btgcpqwovwp","puenodlvotb","jmruuqscwjp","esfmqgvxwfy","utqfcqyrrwm","sxlngbtxmqr","typttkrpfvx","bpoaboylced","bhopoqdsref","vubuucilxyh","kddxywvgqxo","bpeohsufree","lcblwidhjpu","ngbqqmbxqcqp","dwfcayssyoqc","hbuxhwadlpto","phckcyufdqml","shwywshtdgmb","cwkuzyamnerp","xbrtspfttota","paeurdvexqlw","evxtehxtbthq","brxpfymuvfvs","vwduwmjpblqo","jfymrbafmyoc","exlwulswtvot","khxkdxflwxme","fxyfqbeoktcc","hesvnctfvdsp","ebwrcpafxzhb","goabwrqdoudf","vfelxvtggkkk","cnumquohlcgt","nvybsfrxtlfmp","dfuydrtbfypbn","wvpfyfpkvgthq","vtdxwrclpspcn","htedgvsrhchox","oyjmeqvhcrvgm","cwcchvsasdylb","svthrfmkoxbho","sfzdknoxzassc","vqsghhhutdget","dhaccuualacyl","gvyhnchlimsxc","dybjywyaodsyw","gmuyytguexnyc","rlcnvnuuqfvhw","xzluwbtmoxokk","uvouaghhcyvmlk","eqrswgkaaaohxx","thkglauzgkeuly","xhnlcrldtfthul","npdbamofynykqv","fguvomeepxoffg","ukffmudygjavem","mbntqrlwyampdg","khwnykughmwrlk","blolplosqnfcwx","wfrvxqdkhbwwef","gubqavlqffhrzz","lucidbnlysamvy","pwlumocnyuoume","lqdqrrcrwdnxeuo","uxtrdsdfzfssmel","ucgqyvopafyttrh","dutnbetocxylcey","qmqxceuohpiffaq","pmxttqftypfexlv","vlrfcsftapyujmw","mxlwbkbklbwfsvr","tdtuquartspkotm","goblttgvmndkqgg","phknqtsdtwxcktmw","pbqurqfxgqlojmws","upmsoxftumyxifyu","pstsxhplrrmbeddv","sqqoffmwkplsgbrp","yqssxzsydgllfzmo","reogbmveofvusdsx","lplrsxznfkoklxlv"]


b = ["gfve","qfpd","lqdqrrcrwdnxeuo","hbsfyfv","ife","feclhbvfuk","ngbqqmbxqcqp","khhqr","dwfcayssyoqc","omwufbdfxu","ilebxwbcto","ta","hbuxhwadlpto","tpvo","phckcyufdqml","lfz","tgygdt","nhcvpf","shwywshtdgmb","bkkxcvg","monmwvytby","qtg","cwkuzyamnerp","ye","tfsrptug","gama","nberblt","mf","gttxwpuk","xbrtspfttota","qxru","phknqtsdtwxcktmw","pbqurqfxgqlojmws","hdkbdxqg","ge","ukmcowoe","xdnnl","yjyssbsoc","uvouaghhcyvmlk","pbcnmhf","qmmidmvkn","xmywegmtuno","vuzygv","uxtrdsdfzfssmel","eqrswgkaaaohxx","ocedkt","qghoy","wsx","glafbwzdd","ryp","nvybsfrxtlfmp","upmsoxftumyxifyu","xucubv","fctkqlroq","ppvs","nwedtubynsb","repgcx","gsfomhvpmy","kdohe","llkmagl","thkglauzgkeuly","paeurdvexqlw","akdt","rqdll","mumbh","br","fso","qnebmfl","lq","xbhkkfg","ax","gqgsomonv","reqqzzpw","rlbskqgfvn","lfvobeyolyy","mwrvel","ogwilaswn","yw","egdgye","yaqgault","dtlg","iddymnl","evxtehxtbthq","brxpfymuvfvs","rv","udvmara","fecd","dfuydrtbfypbn","cypqodxr","vkmxys","wvpfyfpkvgthq","av","vwduwmjpblqo","xwnbcuggl","flhyfac","mqrbq","pstsxhplrrmbeddv","hnegtuxx","bhhlovgcx","had","aysulvk","potn","os","np","lhv","uzvgyeette","tp","wtsbhgkd","eouxbldsxzm","xhnlcrldtfthul","xhflc","rlaks","phouoyhvls","dqhqats","koat","pybf","po","wygsnxk","kqlima","fgxnuohrnhg","wnnbq","mdtrgv","nkq","agylw","vomtuy","vtdxwrclpspcn","rdrls","yxfeoh","myctacn","fdnor","qfzwuwe","svo","dc","odknlbvxrs","hwc","erpbaxq","rrklkb","wlrwyuy","yyhga","xwdbycdu","htedgvsrhchox","wr","suhesetv","qcagsyqggcf","wljmg","npdbamofynykqv","lmq","oyjmeqvhcrvgm","nxtsnason","gbndakaq","hrtbfnq","fguvomeepxoffg","mat","onlvy","cwcchvsasdylb","dphbfaal","mabkapuoud","vl","ffjfb","svthrfmkoxbho","cvet","ucgqyvopafyttrh","vruh","ukffmudygjavem","dccamymhp","kmm","sc","soqlh","gcdqbcdwbwa","gadgt","pgowefka","cpdxf","sox","fq","lfnrhgsxkhx","loc","fkglorkkvx","ggk","nraoenhd","rrbhfwohfv","yoifoyg","ahmv","byyvhgh","hyw","kedhvwy","rglnpxfqwu","su","mbntqrlwyampdg","jfymrbafmyoc","rhymsno","rkbdlchs","ocbbwwd","exlwulswtvot","tlnc","eo","ua","khxkdxflwxme","kk","cw","pxnktxkm","aa","ngrwqpoh","rwuvd","eruffmlg","bxzovyew","hyfrdngjf","ly","pfgsp","akyprzzphew","ubheeqt","rmbxlcmn","apsbu","khwnykughmwrlk","mvndmua","nlwpw","btgcpqwovwp","sfzdknoxzassc","fg","vhfsf","tyff","blolplosqnfcwx","uwkl","puenodlvotb","naefganqo","cymbrl","wrxw","htknfa","wfrvxqdkhbwwef","vqsghhhutdget","wpccoa","nx","bilt","wqqatye","bwsezd","ww","ss","jmruuqscwjp","nxbk","wd","cfq","gubqavlqffhrzz","caybc","dhaccuualacyl","mtkewbprs","oncggqvr","sqqoffmwkplsgbrp","afumtqugec","nxlbkak","fd","ueolqk","esfmqgvxwfy","npbep","yqssxzsydgllfzmo","tovdtkr","hdykehkefp","ordxzm","dutnbetocxylcey","cr","ngzdc","fxyfqbeoktcc","walsx","brdeumb","dnrrgmem","gvyhnchlimsxc","qe","qm","lt","utqfcqyrrwm","wtelvsqrru","qmqxceuohpiffaq","pmxttqftypfexlv","tg","qa","tccvslp","coqs","oa","lxu","ykbcn","hesvnctfvdsp","ku","at","sxlngbtxmqr","wqrom","krvnaf","hfl","typttkrpfvx","nxqmxr","dhthp","eyelg","npsoqsw","reogbmveofvusdsx","yu","pknt","ckorgrm","bpoaboylced","dmoerc","bhopoqdsref","tmnm","cre","vlrfcsftapyujmw","bcxw","eaum","dybjywyaodsyw","lmu","eocfru","fump","oxpmplpcg","qevdyd","gmuyytguexnyc","lmg","lplrsxznfkoklxlv","twn","bhqultkyfq","saeq","xbuw","kng","uoay","kfykd","armuwp","gtghfxf","pbdrx","adoshnx","rqyex","ng","sid","re","vep","ebwrcpafxzhb","opvrnx","vubuucilxyh","rlcnvnuuqfvhw","goabwrqdoudf","wuznnlyd","vfelxvtggkkk","mxlwbkbklbwfsvr","advraqovan","smkln","kddxywvgqxo","syxngevs","mwo","vg","bpeohsufree","lucidbnlysamvy","urbrmmadea","hghv","gu","uztnpqhdl","rfuyp","xbspa","cnumquohlcgt","tdtuquartspkotm","ugrloq","fkyvqguqq","yy","pwlumocnyuoume","goblttgvmndkqgg","lcblwidhjpu","kbu","pey","bc","lqs","xzluwbtmoxokk","lehdfnr","wruqc","wcbm"]

for aa in a:
    if aa not in b:
        print(aa)
for bb in b:
    if bb not in a:
        priint(bb)
    else:
        print(True)
from collections import Counter
c_a = Counter(a)
c_b = Counter(b)
