class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        def dfs(length: int, n: int) -> List[str]:
            if length == 0:
                return [""]

            if length == 1:
                return ["0", "1", "8"]
            
            res = []

            for num in dfs(length - 2, n):
                for pair in [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]:
                    
                    #if length is n, we cannot add "0" as the first character
                    if length != n or pair[0] != "0":
                        res.append(pair[0] + num + pair[1])
            return res
        
        return dfs(n, n)
