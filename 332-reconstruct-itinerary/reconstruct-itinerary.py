class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # O(N log N), O(N)
        
        adj = defaultdict(list)

        for dep, arr in sorted(tickets, reverse=True):
            adj[dep].append(arr) # reverse sorted to use pop efficiently

        st = ["JFK"]
        res = []

        while st:
            # If the current airport (top of stack) has remaining destinations, add the next one to the stack
            if adj[st[-1]]:
                st.append(adj[st[-1]].pop())
            else:
                # If there are no more destinations, add the current airport to the new itinerary
                res.append(st.pop())

        # Reverse the result
        return res[::-1]
