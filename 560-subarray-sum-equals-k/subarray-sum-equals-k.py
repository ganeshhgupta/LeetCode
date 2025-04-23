class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        #maintain a map : prefix sum (curr_sum - k) -> count

        res = curr = 0
        prefixSum = { 0 : 1 }

        for n in nums:
            curr += n
            diff = curr - k

            if diff in prefixSum:
                res += prefixSum[diff]

            if curr in prefixSum:
                prefixSum[curr] += 1
            else:
                prefixSum[curr] = 1
            
        return res
