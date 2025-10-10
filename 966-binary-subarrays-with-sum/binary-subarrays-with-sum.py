class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # O(n), O(n)
        map = defaultdict(int)
        map[0] = 1 # can sum upto 0 in atleast 1 way
        curr = res = 0

        for n in nums:
            curr += n
            diff = curr - goal

            if map[diff]: res += map[diff]
            map[curr] += 1
        
        return res