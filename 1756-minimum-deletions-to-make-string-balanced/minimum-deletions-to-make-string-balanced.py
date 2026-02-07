class Solution:
    def minimumDeletions(self, s: str) -> int:

        res = 0   # total deletions made so far
        b_cnt = 0     # number of b's kept so far

        for ch in s:
            if ch == 'b':
                # keep b for now
                b_cnt += 1
            else:
                # ch == 'a' after some b's
                # either delete this a (del_cnt + 1)
                # or delete all previous b's (b_cnt)
                res = min(res + 1, b_cnt)

        return res
