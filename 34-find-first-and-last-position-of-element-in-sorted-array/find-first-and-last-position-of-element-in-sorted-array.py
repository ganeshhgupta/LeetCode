class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def helper( side ):

            low, high = 0, len(nums) - 1
            found = -1
            while low <= high:
                mid = (high + low) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    found = mid
                    if side == "left":
                        high = mid - 1
                    else:
                        low = mid + 1
            return found

        first = helper("left")
        second = helper("right") 

        return [first, second]
                