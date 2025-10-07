class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        # O(nlogn), O(n)
        self.count = 0
        def merge(l, r):

            i, j = 0, 0
            while i < len(l) and j < len(r):
                if l[i] > 2 * r[j]:
                    self.count += len(l) - i # count satisfying pairs
                    j += 1
                else: i += 1

            i = j = 0
            res = []
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1
            res.extend(l[i:])
            res.extend(r[j:])
            return res

        def split(n):
            if len(n) <= 1: return n
            mid = len(n)//2
            l, r = split(n[:mid]), split(n[mid:])
            return merge(l, r)

        nums = split(nums)
        return self.count