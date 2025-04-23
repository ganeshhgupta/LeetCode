class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        pre_l = [1] * n
        post_l = [1] * n
        pre = post = 1

        for i in range(n):
            pre *= nums[i]
            pre_l[i] = pre
        for i in reversed(range(n)):
            post *= nums[i]
            post_l[i] = post
        print(pre_l, post_l)
        for i in range(1, n - 1):
            print(pre_l[i], post_l[i])
            res[i] = pre_l[i - 1] * post_l[i + 1]
        res[0] = post_l[1]
        res[-1] = pre_l[n-2]
        return res