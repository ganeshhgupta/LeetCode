class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()
        n = len(nums)
        count = 0
        
        def bin(target, l, r):
            print(target)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        print(lower, " <= x <= ", upper)
        for i in range(n):

            lb = bin(lower - nums[i], i + 1, n)
            rb = bin(upper - nums[i] + 1, i + 1, n)
            if lb < n and rb - 1 < n:
                print( nums[lb], nums[i], nums[rb - 1])
            count += rb - lb
        
        return count

