class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # O(n), O(n)
        n = len(nums)
        pre = [1] * n
        post = [1] * n

        for i in range(1, n): # calc and shift pref prod by 1 to the right
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(n-2, -1, -1): # calc and shift postf prod by 1 to the left
            post[i] = post[i+1] * nums[i+1]

        res = [pre[i] * post[i] for i in range(n)] # multiply as is
        return res
