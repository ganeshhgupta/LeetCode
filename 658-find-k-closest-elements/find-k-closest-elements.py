class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        def binary_search(arr, x):
            l, r = 0, len(arr) - 1  

            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == x:
                    return mid 
                elif arr[mid] < x:
                    l = mid + 1  
                else:
                    r = mid - 1  
            return l

        i = binary_search(arr, x)  #closest insert position of x

        l, r = i - 1, i
        res = []

        while len(res) < k:
            ld = rd = float('inf')

            if l >= 0:
                ld = abs(arr[l] - x)

            if r < len(arr):
                rd = abs(arr[r] - x)

            if ld <= rd:
                res.append(arr[l])
                l -= 1 
            else:
                res.append(arr[r])
                r += 1 

        return sorted(res)
