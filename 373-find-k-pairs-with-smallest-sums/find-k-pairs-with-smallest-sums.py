class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # O (k log k), O(k)
        # min heap
        
        if not nums1 or not nums2:
            return []
        
        n1, n2 = len(nums1), len(nums2)
        mh = [(nums1[0] + nums2[0], 0, 0)] # (sum, i, j)
        v = {(0, 0)}
        res = []

        while mh and len(res) < k:

            val, i, j = heapq.heappop(mh)
            res.append([nums1[i], nums2[j]])

            if i + 1 < n1 and (i + 1, j) not in v:
                heapq.heappush(mh, (nums1[i + 1] + nums2[j], i + 1, j))
                v.add((i + 1, j))
            if j + 1 < n2 and (i, j + 1) not in v:
                heapq.heappush(mh, (nums1[i] + nums2[j + 1], i, j + 1))
                v.add((i, j + 1))
        
        return res

