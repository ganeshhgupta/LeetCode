class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()

        available = [i for i in range(n)] # heap to store currently avail rooms (rn all)
        used = [] # (end_time, room_no.)  # heap to store currently used rooms (rn all)
                  # top of the heap would always have to room that's closest to being empty

        count = [0] * n # keep track of (meeting room : no. of times used)

        for start, end in meetings:

            # finish any meetings that end at current 'start' time:
            while used and start >= used[0][0]: # first [0] for heap top, second [0] for end_time from (end_time, room_no.)

                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # no room available (wait till earliest end_time)
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(available, room)

            # room available (at this point it has to be available):
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
        
        return count.index(max(count))







