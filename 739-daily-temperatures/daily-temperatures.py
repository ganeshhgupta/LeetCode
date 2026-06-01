class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # O(n), O(n)
        
        res = [0] * len(temperatures)
        st = [] # (idx, temp)

        for i, t in enumerate(temperatures):

            while st and st[-1][1] < t: # when curr t > st[-1] t : popping happens
                idx, temp = st.pop()
                res[idx] = i - idx
            
            st.append((i, t))

        return res
             
