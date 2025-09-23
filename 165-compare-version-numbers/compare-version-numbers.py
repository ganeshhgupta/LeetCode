class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2 = version1.split("."), version2.split(".")
        
        max_len = max(len(l1), len(l2))
        l1 += ["0"] * (max_len - len(l1))
        l2 += ["0"] * (max_len - len(l2))
        
        for i in range(max_len):
            n1, n2 = int(l1[i]), int(l2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        
        return 0
