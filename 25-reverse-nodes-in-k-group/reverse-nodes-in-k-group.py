# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        c, t = 0, head

        while t and c < k: # count out k nodes and then
            t = t.next
            c += 1
        
        if c < k:
            return head
        
        def rev(s, e): # simply rev the LL
            prev, curr = None, s
            while curr != e:
                t = curr.next
                curr.next = prev
                prev = curr
                curr = t
            return prev
        
        new_head = rev(head, t)
        head.next = self.reverseKGroup(t, k)
        return new_head
