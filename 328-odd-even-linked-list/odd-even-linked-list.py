# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(n), O(1)
        if not head: return 
        o = head
        e_head = e = head.next

        while e and e.next:
            o.next = o.next.next
            o = o.next
            e.next = e.next.next
            e = e.next

        o.next = e_head
        return head





