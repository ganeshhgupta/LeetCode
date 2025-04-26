class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        mh = []

        for i in range(len(nums)):
            heapq.heappush(mh, (nums[i], i))
        
        for i in range(k):
            m, j = heapq.heappop(mh)
            heapq.heappush(mh, (m * multiplier, j))

        for m, j in mh:
            nums[j] = m 
            
        return nums