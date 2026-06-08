class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # O(n), O(n)
        
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
