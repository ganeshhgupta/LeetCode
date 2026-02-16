class Solution:
    def __init__(self):
        self.fact = []
        self.digits = []

    def solve(self, ans, n, k):
        if n == 1:
            ans.append(str(self.digits[-1]))
            return
        
        index = k // self.fact[n - 1]
        
        if k % self.fact[n - 1] == 0:
            index -= 1
            
        ans.append(str(self.digits[index]))
        self.digits.pop(index)
        
        k -= self.fact[n - 1] * index
        self.solve(ans, n - 1, k)

    def getPermutation(self, n: int, k: int) -> str:
        self.fact = [1]
        f = 1
        for i in range(1, n):
            f *= i
            self.fact.append(f)
            
        self.digits = [i for i in range(1, n + 1)]
        
        ans = []
        self.solve(ans, n, k)
        return "".join(ans)