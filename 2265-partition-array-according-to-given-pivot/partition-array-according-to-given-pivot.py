class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        l1 = []
        l2 = []
        l3 = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                l1.append(nums[i])
            elif nums[i] == pivot:
                l2.append(nums[i]) 
            else:
                l3.append(nums[i])

        print(l1, l2, l3)
        return l1 + l2 + l3

    # 9,12,5,10,14,3,10

    #bubbling left to right:

    #9,5, 12,10,14,3,10
    #9,5, 10,12,14,3,10
    #9,5, 10,12,14,3,10

    #9,5, 10,12,3,14,10
    #9,5, 10,12,3,10,14

    #right to left

    #9,5, 10,12,3,14,10
    #9,5, 10,12,3,10,14
     #9,5, 10,3,10,12,14
    #9,5, 3, 10,10,12,14