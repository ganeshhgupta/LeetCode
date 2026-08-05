class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # O(n)
        # dummy handles duplicate head cases
        # prev points to last unique node in result
        # curr scans list, skip all duplicate values

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:

            if curr.next and curr.val == curr.next.val:

                # skip all nodes with this duplicate value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                prev.next = curr.next

            else:
                prev = prev.next

            curr = curr.next

        return dummy.next