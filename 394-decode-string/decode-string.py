class Solution:
    def decodeString(self, s: str) -> str:

        # two stack, O(n), O(n)
        
        nums = []
        strs = []
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                nums.append(num)
                strs.append(curr)
                num = 0
                curr = ""

            elif ch == ']':
                curr = strs.pop() + nums.pop() * curr

            else:
                curr += ch

        return curr