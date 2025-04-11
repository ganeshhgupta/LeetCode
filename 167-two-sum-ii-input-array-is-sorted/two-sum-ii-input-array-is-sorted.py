class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:
            # since array is sorted, shift l if sum<target, r if sum>target
            # it says solution is guarenteed hence while l < r
            sum = numbers[l] + numbers[r] 
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l+1, r+1]