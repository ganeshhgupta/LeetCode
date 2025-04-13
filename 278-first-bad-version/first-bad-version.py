# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l, r = 1, n
        while l < r:

            mid = ( l + r - 1) // 2

            if isBadVersion(mid) == True:
                r = mid # cause first bad version could be this itself
            else:
                l = mid + 1 # we don't care about skipping good version

        return l
