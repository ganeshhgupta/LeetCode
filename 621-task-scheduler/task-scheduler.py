class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # O(n), O(1)
        freq = Counter(tasks)        
        max_count = max(freq.values())        
        max_count_tasks = list(freq.values()).count(max_count)
        
        # Compare with total tasks, since sometimes all gaps can be filled
        intervals = (max_count - 1) * (n + 1) + max_count_tasks
        
        return max(len(tasks), intervals)
