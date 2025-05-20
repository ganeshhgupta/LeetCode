# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        f, s = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s
        prev = temp = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        s = head
        while prev:
            if s.val != prev.val:
                return False
            s = s.next
            prev = prev.next
        return True