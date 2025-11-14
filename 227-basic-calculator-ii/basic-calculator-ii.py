class Solution:
    def calculate(self, s: str) -> int:
        curr = prev = res = 0 
        op = '+'
        s += '+'  #add an operator '+' to ensure the last number is processed

        for ch in s:

            if ch.isdigit():
                curr = curr * 10 + int(ch)

            elif ch in "+-*/":
                
                if op == '+':
                    res += prev
                    prev = curr # prev stores the previous curr for one iteration
                                # just to mmake sure, if next op is '*' or '/' it'll immediately perform it
                                # if op is '+'/'-' it'll add/subtract the previous curr to res

                elif op == '-':
                    res += prev
                    prev = -curr

                elif op == '*':
                    prev *= curr

                elif op == '/':
                    prev = int(prev / curr)  # Truncate toward zero

                op = ch
                curr = 0

            elif ch == ' ':
                continue

        res += prev
        return res
