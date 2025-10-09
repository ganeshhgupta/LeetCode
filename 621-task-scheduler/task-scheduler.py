from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        max_count = max(freq.values())
        
        # Count how many tasks have this highest frequency
        max_count_tasks = list(freq.values()).count(max_count)
        
        # Formula: (max_count - 1) * (n + 1) + max_count_tasks
        # Compare with total tasks, since sometimes all gaps can be filled
        intervals = (max_count - 1) * (n + 1) + max_count_tasks
        
        return max(len(tasks), intervals)
