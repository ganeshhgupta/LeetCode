class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n == 2:
            return [-1, 1]
        li = []
        for i in range(n - 1):
            li.append(i)
        li.append(-(sum(li)))
        return li