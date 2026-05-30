class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # O(n), O(n)
        # two pass, we can always remove the last '('s

        res = []
        c = 0 # extra ( param

        # first pass to remove extra ):

        for i in s:
            if i == '(':
                c += 1
                res.append(i)
            
            elif i == ')' and c > 0:
                c -=1
                res.append(i)

            elif i != ')':
                res.append(i) # reg chars
        
        filtered = []
        res = reversed(res)

        # second pass to remove extra (:

        for i in res:
            if i == '(' and c > 0:
                c -= 1
            else:
                filtered.append(i)
        
        return "".join(filtered[::-1])


