import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        mh = []
        for node in lists:
            if node:
                heapq.heappush(mh, (node.val, id(node), node))

        dummy = ListNode(0)
        curr = dummy

        while mh:
            val, node_id, node = heapq.heappop(mh)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(mh, (node.next.val, id(node.next), node.next))
        
        return dummy.next
