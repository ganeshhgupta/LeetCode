class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        offline_until = [0] * numberOfUsers

        # Group events by timestamp (int)
        events_by_time = defaultdict(list)
        for eve, timestamp, content in events:
            events_by_time[int(timestamp)].append((eve, content))

        # Process timestamps in order
        for t in sorted(events_by_time.keys()):
            # 1) Auto bring users online whose offline window ended at or before t
            for i in range(numberOfUsers):
                if not online[i] and offline_until[i] <= t:
                    online[i] = True

            # 2) Apply all OFFLINE events at this timestamp first
            for eve, content in events_by_time[t]:
                if eve == "OFFLINE":
                    uid = int(content)
                    online[uid] = False
                    offline_until[uid] = t + 60

            # 3) Then handle all MESSAGE events at this timestamp
            for eve, content in events_by_time[t]:
                if eve != "MESSAGE":
                    continue

                tokens = content.split()
                for token in tokens:
                    if token == "ALL":
                        for i in range(numberOfUsers):
                            mentions[i] += 1
                        continue

                    if token == "HERE":
                        for i in range(numberOfUsers):
                            if online[i]:
                                mentions[i] += 1
                        continue

                    if token.startswith("id"):
                        uid = int(token[2:])
                        mentions[uid] += 1

        return mentions
