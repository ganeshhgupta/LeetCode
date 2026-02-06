# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        # Step 1: convert linked list to array
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        
        n = len(nums)
        answer = [0] * n
        stack = []  # stores indices
        
        # Step 2: use monotonic decreasing stack
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                answer[index] = nums[i]
            stack.append(i)
        
        return answer
