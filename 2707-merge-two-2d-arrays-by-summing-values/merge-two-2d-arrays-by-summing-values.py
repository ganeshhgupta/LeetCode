from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        map = {}

        for index, val in nums1:
            map[index] = map.get(index, 0) + val
        
        for index, val in nums2:
            map[index] = map.get(index, 0) + val

        sorted_map = sorted(map.items())
        result = [] 

        for id_, value in sorted_map:
            result.append([id_, value]) 

        return result
