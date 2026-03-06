class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        # O(2^n), O(n)
        self.res = []
        self.max_len = 0

        def dfs(i, li, l, r):
            if i == len(s):
                if l == r:
                    curr = ''.join(li)
                    if len(curr) > self.max_len:
                        self.max_len = len(curr)
                        self.res = [curr]
                    elif len(curr) == self.max_len:
                        self.res.append(curr)
                return

            c = s[i]
            
            if c not in '()':
                dfs(i + 1, li + [c], l, r)
            elif c == '(':
                # choice 1: keep '('
                dfs(i + 1, li + ['('], l + 1, r)
                # choice 2: skip '('
                dfs(i + 1, li, l, r)
            elif c == ')':
                if r < l:
                    # choice 1: keep ')'
                    dfs(i + 1, li + [')'], l, r + 1)
                # choice 2: skip ')'
                dfs(i + 1, li, l, r)

        dfs(0, [], 0, 0)
        return list(set(self.res))