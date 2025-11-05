class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
            # O (2^ (k*n)), O (n)
            # target sum + visited + k times
            
            n = len(nums)
            nums.sort(reverse=True)
            total = sum(nums)
            
            if total % k != 0:
                return False
            
            target = int(total / k)
            used = [False] * n
            
            def dfs(index, total, k): 
                
                if k == 0:
                    return True
                
                if total == 0:
                    return dfs(0, target, k - 1)
                
                for i in range(index, n):
                    
                    if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                        continue
                        
                    if used[i] or total - nums[i] < 0:
                        continue
                    
                    used[i] = True
                    if dfs(i + 1, total - nums[i], k):
                        return True
                    used[i] = False
                return False
            
            return dfs(0, target, k)