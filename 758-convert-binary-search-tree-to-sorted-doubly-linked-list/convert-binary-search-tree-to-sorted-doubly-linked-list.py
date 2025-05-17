class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return
        
        head, tail = None, None

        def dfs(node):
            nonlocal head, tail
            if not node:
                return
            
            dfs(node.left)

            if tail:
                tail.right = node
                node.left = tail
            else:
                head = node

            tail = node
            
            dfs(node.right)
        

        dfs(root)

        head.left = tail
        tail.right = head
        
        return head