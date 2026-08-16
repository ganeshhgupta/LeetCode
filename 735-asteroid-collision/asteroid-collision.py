class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # O(n), O(n)
        
        st = []

        for a in asteroids:

            while st and st[-1] > 0 and a < 0: # if st[-1] going R, a going L ( -ve L, +ve R )

                if abs(st[-1]) < abs(a): # if a wins, pop st[-1]
                    st.pop()
                    continue

                elif abs(st[-1]) == abs(a): # if tie, we pop st[-1] and make a = 0 so line 23: if a : fails
                    st.pop()
                    a = 0
                
                else:
                    a = 0
            
            if a:
                st.append(a)
            
        return st

        '''
        There are two cases where a gets destroyed:

        elif st[-1] == abs(a):
            st.pop()      # stack asteroid also destroyed
            a = 0         # current asteroid destroyed

        Both asteroids disappear. And:

        else:
            a = 0         # stack asteroid is bigger, so current asteroid dies

        We use a = 0 so that after the while loop:

        if a:
            st.append(a)

        does not add the destroyed asteroid back to the stack.
        '''