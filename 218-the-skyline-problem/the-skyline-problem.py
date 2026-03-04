class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        # O(n), O(n)
        
        events = []
        for L, R, H in buildings:
            events.append((L, -H)) # starting event, for max heap of H
            events.append((R, H)) # ending event
        
        events.sort()

        res = []
        mh = [0] # start with height 0, max-heap via -ve values
        heapq.heapify(mh)

        removed = defaultdict(int)
        prev_h = 0

        for x, h in events:

            if h < 0: # only add starting events
                heapq.heappush(mh, h)
            else:
                removed[-h] += 1
        
            while mh and removed[ mh[0] ] > 0:
                removed[ mh[0] ] -= 1
                heapq.heappop(mh)
            
            curr_h = - mh[0]

            if curr_h != prev_h:
                res.append([x, curr_h])
                prev_h = curr_h

        return res        

