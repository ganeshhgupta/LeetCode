class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, first, second, gain):
            stack = []
            res = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    res += gain
                else:
                    stack.append(c)
            return ''.join(stack), res

        if x > y:
            s, gain1 = remove_pair(s, 'a', 'b', x)
            _, gain2 = remove_pair(s, 'b', 'a', y)
        else:
            s, gain1 = remove_pair(s, 'b', 'a', y)
            _, gain2 = remove_pair(s, 'a', 'b', x)

        return gain1 + gain2
