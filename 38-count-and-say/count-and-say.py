class Solution:
    def countAndSay(self, n: int) -> str:
        
        ans = "1"

        if n == 1:
            return "1"

        else:
            for i in range(1, n):
                ans = self.RLE(ans)
                print(ans)

            return ans

    def RLE(self, n: str) -> str:
        li = []
        c = 1

        if len(n) == 1:
            return "1" + n

        for i in range(len(n)):
            if i < len(n) - 1:

                if n[i] != n[i + 1]:
                    li.append(str(c))
                    li.append(n[i])
                    c = 1
                else:
                    c += 1
            else:
                li.append(str(c))
                li.append(n[i])

        return ''.join(li)
