class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # O(n), O(n)

        st = [] # (idx, temp)
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while st and st[-1][1] < temp:
                st_i, st_temp = st.pop()
                res[st_i] = i - st_i

            st.append((i, temp))
        
        return res

