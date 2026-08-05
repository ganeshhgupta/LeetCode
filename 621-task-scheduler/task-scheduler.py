class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # don't worry about chars, just their cnts
        # max heap to always pick the highest freq available task
        # use timestamp counter and queue to track tasks in cooldown
        # after executing task, decrease cnt and add it to queue with next available time
        # when cooldown expires, push task back into heap
        # keep increasing time until heap and cooldown queue are empty

        count = Counter(tasks)
        mh = [-cnt for cnt in count.values() ]
        heapq.heapify(mh)

        time = 0
        q = deque() # [-cnt, idleTime]

        while mh or q:
            time += 1

            if mh:
                cnt = 1 + heapq.heappop(mh)
                
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(mh, q.popleft()[0])
        
        return time


