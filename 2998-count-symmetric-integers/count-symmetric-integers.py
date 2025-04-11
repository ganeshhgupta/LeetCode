class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        if len(str(low)) % 2 == 1:
            low = 10 ** len(str(low))
        if len(str(low)) % 2 == 1:
            low = 10 ** len(str(low) - 1)

        print(low, high)

        def sum(lst):
            result = 0
            for num in lst:
                result += int(num)
            return result

        count = 0

        for i in range(low, high + 1):
            li = list(str(i))
            if len(li) % 2 == 0:
                mid = len(li)//2
                if sum(li[:mid]) == sum(li[mid:]):
                    count += 1
                    print(i, li[:mid], li[mid:] )

        return count