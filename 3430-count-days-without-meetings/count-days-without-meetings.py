class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meet_end = 0
        n = len(meetings) - 1
        meetings = sorted(meetings, key=lambda x: x[0])
        print(meetings)
        #print(meetings[0][0])
        count = (meetings[0][0] - 1)
        print("count: ", count)
        for i in range(len(meetings)-1):
            meet_end = max(meet_end, meetings[i][1])
            #print(meet_end)
            print(meetings[i][1] , meet_end, meetings[i+1][0])
            if meetings[i][1] < meetings[i+1][0] and meetings[i+1][0] > meet_end:
                count += ((meetings[i+1][0]) - max(meet_end, meetings[i][1]) - 1)
                print("count: ", count)

        meet_end = max(meet_end, meetings[-1][1])
        print(days, meet_end)
        count += (days - meet_end)
        print("count: ", count)
        return count