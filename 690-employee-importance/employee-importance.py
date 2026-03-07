"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        # O(n), O(n)
        # we don’t need any employee above the given ID
        # bfs to add imp cumulatively from all children, return total imp

        e_map = {e.id: e for e in employees}
        
        q = deque([id])
        res = 0
        
        while q:
            curr = q.popleft()
            emp = e_map[curr]
            
            res += emp.importance
            
            for sub in emp.subordinates:
                q.append(sub)
        
        return res