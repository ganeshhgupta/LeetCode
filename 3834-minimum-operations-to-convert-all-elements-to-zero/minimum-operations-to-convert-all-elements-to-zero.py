class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # O(n), O(n)

        st = []
        res = 0

        for val in nums:

            if val == 0:
                st.clear()
                continue
            
            while st and st[-1] > val:
                st.pop()
            
            if st and st[-1] == val:
                continue
            
            st.append(val)
            res += 1
        
        return res

'''
always keep adding n[i] to stack unless st[-1] == n[i]

every add acts as an operation (i acts as the starting index of that operation, the end index will be when we encounter a value < n[i])

when st[-1] > n[i]: st[-1] would need an isolated operation, so pop it off, and keep poppnig untill st[-1] <= n[i]

when st[-1] < n[i]: just add n[i] to stack, we readily add its operation anyway

when n[i] == 0, since 0 is a wall, pop of everything in the st up untill that point

'''