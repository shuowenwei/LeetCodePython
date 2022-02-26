# -*- coding: utf-8 -*-
"""
@author: Wei, Shuowen

https://leetcode.com/problems/accounts-merge/

"""
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        all_emails = {}
        for acct in accounts:
            for index, email in enumerate(acct):
                name = acct[0]
                if index != 0:
                    all_emails[email] = name
        n = len(all_emails)
        email2index = [email for email in all_emails.keys()]
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        self.count = n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(p, q):
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]
            self.count -= 1
        for acct in accounts:
            for index, email in enumerate(acct):
                name = acct[0]
                primary_email = acct[1]
                if index not in (0, 1):
                    # print(primary_email, email)
                    # print(email2index.index(primary_email), email2index.index(email))
                    union(email2index.index(primary_email), email2index.index(email))
        # print(parent, size, self.count)
        dct_emails_groups = collections.defaultdict(list)
        
        for index, email in enumerate(email2index):
            email_parent = email2index[find(index)] # must use find(), can't use parent[]
            dct_emails_groups[email_parent].append(email)
        res = []
        for k, v in dct_emails_groups.items():
            tmp = [all_emails[k]] + sorted(v)
            res.append(tmp)
        return res
    