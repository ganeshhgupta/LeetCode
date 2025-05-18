
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
    
        total = sum(nums)  
        count = Counter(nums)
        max_o = float('-inf')
        #outlier=total_sum−2×sum of special number
        for num in count.keys():
            curr_o = total - 2 * num  
            if curr_o in count:
                if curr_o != num or count[num] > 1: 
                    max_o = max(max_o, curr_o)
        return max_o