# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()       # Dummy node to start the merged list
        curr = dummy             # Pointer to build the result list

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

        '''
        Every time we do:

        curr.next = list1 or list2
        curr = curr.next

        We’re linking nodes to the .next of curr, which is really just building off of the .next of dummy.

        So if you visualize it:

        dummy -> node1 -> node2 -> node3 ...
        Even though curr keeps moving forward, dummy always stays at the start.

        Why return dummy.next?
        Because dummy was just a placeholder node (usually with value 0), we don’t want to include it in the final answer.

        So we return:
        
        return dummy.next  # The real start of our merged list
        '''