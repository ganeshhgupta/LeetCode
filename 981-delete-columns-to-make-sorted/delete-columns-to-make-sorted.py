class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        res = 0
        n = len(strs) 
                
        columns = list(zip(*strs))
        print(columns)
        for col in columns:
            print(col,tuple(sorted(col)))
            if col != tuple(sorted(col)):
                res += 1
        return res

           
        
