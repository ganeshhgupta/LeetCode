class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(idx, curr_res, curr_sum, prev_val):
            if idx >= len(num):
                if curr_sum == target:
                    res.append("".join(curr_res))
                    return
            for i in range(idx, len(num)):
                curr_str = num[idx : i + 1]
                curr_num = int(curr_str)
                
                if not curr_res:
                    dfs( i + 1, [curr_str], curr_num, curr_num)
                else:
                    dfs( i + 1, curr_res + ["+"] + [curr_str], curr_sum + curr_num, curr_num)
                    dfs( i + 1, curr_res + ["-"] + [curr_str], curr_sum - curr_num, -curr_num)
                    dfs( i + 1, curr_res + ["*"] + [curr_str], curr_sum - prev_val + curr_num * prev_val , curr_num * prev_val)
                
                if num[idx] == '0':
                    break
        dfs(0, [], 0, 0)

        return res