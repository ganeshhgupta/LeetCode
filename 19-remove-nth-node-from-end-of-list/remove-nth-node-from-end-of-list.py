class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        i = 0
        
        # len(list)
        while curr:
            i += 1
            curr = curr.next
        
        n = i - n
        
        #If we need to remove the head node
        if n == 0:
            return head.next
        
        #Traverse again to find the (i-n)-th node
        curr = head
        while n > 1:
            curr = curr.next
            n -= 1
        
        #Remove the n-th node
        curr.next = curr.next.next
        
        return head
