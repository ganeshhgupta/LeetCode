class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0]

        #res = [0,1,1,2,1,2,..]
        # for every ith number, no. of 1s = no. of 1s in i/2th number, then add 1 if it is odd
        # since i/2 is just a right shift of i
        #https://www.youtube.com/watch?v=awxaRgUB4Kw
        
        for i in range(1, n + 1):

            if i % 2 == 0:
                res.append(res[i//2])
            else:
                res.append(res[i//2] + 1)

        return res
