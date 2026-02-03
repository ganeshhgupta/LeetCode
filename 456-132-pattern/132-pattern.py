class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        # O(n), O(n)
        # mono desc stack
        
        st = [] # (num, leftMin)
        currMin = nums[0]

        for n in nums[1:]:

            while st and n >= st[-1][0]:
                st.pop()

            if st and n > st[-1][1]:
                return True

            st.append([n, currMin])
            currMin = min(n, currMin)
        
        return False