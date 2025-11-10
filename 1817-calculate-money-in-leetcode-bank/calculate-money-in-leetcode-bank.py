class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        res = weeks * 28     +    7 * weeks * (weeks - 1) // 2

        # Last day's money in the last full week
        last_day_money = weeks  # last week starts with full_weeks, ends at full_weeks + 6

        # Add leftover days
        for i in range(1, days + 1):
            res += last_day_money + i

        return res
