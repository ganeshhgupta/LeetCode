class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        n = len(nums)
        answer = []
        
        for i in range(n - k + 1):
            # Get the current subarray
            subarray = nums[i:i + k]
            
            # Count frequencies
            freq = {}
            for num in subarray:
                freq[num] = freq.get(num, 0) + 1
            
            # If less than x distinct elements, return sum of all
            if len(freq) < x:
                answer.append(sum(subarray))
                continue
            
            # Sort by frequency (descending), then by value (descending)
            # This gives us the "top x most frequent elements"
            sorted_items = sorted(freq.items(), key=lambda item: (item[1], item[0]), reverse=True)
            
            # Take top x elements and calculate their sum
            x_sum = 0
            for j in range(x):
                num, count = sorted_items[j]
                x_sum += num * count
            
            answer.append(x_sum)
        
        return answer