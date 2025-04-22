class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  #Each element is [char, count]

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # Remove k duplicates
            else:
                stack.append([char, 1])

        return ''.join(char * count for char, count in stack)
