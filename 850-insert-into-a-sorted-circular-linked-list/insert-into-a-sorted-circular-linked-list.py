"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
                    
        curr = head
        dummy = Node(insertVal)

        if not head:
            dummy.next = dummy
            return dummy

        while curr.next != head:
            if curr.val <= insertVal <= curr.next.val:
                dummy.next = curr.next
                curr.next = dummy
                return head
            
            elif curr.val > curr.next.val:
                if curr.val <= insertVal or insertVal <= curr.next.val:
                    dummy.next = curr.next
                    curr.next = dummy
                    return head

            curr = curr.next

        dummy.next = curr.next
        curr.next = dummy
        return head


        