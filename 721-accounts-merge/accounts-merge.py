class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # O(N + E log E) n - acc, E - emails

        # 1. Map each email to the account where it first appears.
        # 2. If an email appears again, union the two account indices.
        # 3. Group all emails by their Union-Find root.
        # 4. Sort each group and prepend the account name.

        n = len(accounts)
        uf = UF(n)
        email_to_id = {} # {email : index of that entry} 
                         # if an email appears in multiple entries, it will be unioned with its initially found entry

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = i
                else:
                    uf.union(i, email_to_id[email])

        groups = defaultdict(list)

        for email, i in email_to_id.items():
            groups[uf.find(i)].append(email)

        res = []

        for i, emails in groups.items():
            res.append([accounts[i][0]] + sorted(emails))

        return res



class UF:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.par[y] = x
        self.rank[x] += self.rank[y]