class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        q = deque([root])
        res = []

        while q:
            li = []
            for i in range(len(q)):
                n = q.popleft()
                if n:
                    li.append(n)
                    q.append(n.left)
                    q.append(n.right)
            
            if li:
                
                for i in range(len(li) - 1):
                    li[i].next = li[i+1]
                li[-1].next = None
                res.append(li)
        
        return root