class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        map1, map2 = defaultdict(), defaultdict()
        res = []


        for i in nums1:
            if i not in map1:
                map1[i] = 1
            else:
                map1[i] += 1
       
        for i in nums2:
            if i not in map2:
                map2[i] = 1
            else:
                map2[i] += 1 

        for i in map1:
            if i in map2:
                l = min(map1[i], map2[i])
                while l > 0:
                    res.append(i)
                    l -= 1

        return res