class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        mh = []
        i = 0
        day = 1
        attended = 0
        n = len(events)
        last_day = max(end for _, end in events)

        while day <= last_day:
            # Add all events that start today
            while i < n and events[i][0] == day:
                heapq.heappush(mh, events[i][1])
                i += 1

            # Remove expired events
            while mh and mh[0] < day:
                heapq.heappop(mh)

            # Attend the event that ends earliest
            if mh:
                heapq.heappop(mh)
                attended += 1

            day += 1

        return attended
