class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        mid = 0
        left = []
        right = []

        for n in nums:
            if n < pivot:
                left.append(n)
            
            elif n > pivot:
                right.append(n)
            
            else:
                mid += 1
        
        return left + [pivot] * mid + right
