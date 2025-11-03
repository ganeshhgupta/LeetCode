class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        # O((n + extraStudents) × log n), O(n)
        '''
        Step 1: For each class, compute its potential gain if we add one more passing student.
        Step 2: Push all gains into a max heap (store negative values since Python’s heapq is a min-heap).
        Step 3: While extra students remain:
            Pop the class with highest gain.
            Update its pass and total counts (p += 1, t += 1).
            Recompute its new gain and push back into heap.
        Step 4: After assigning all extra students, compute the final average pass ratio.
        '''    
        def gain(p, t):
            return (p+1)/(t+1) - p/t
        
        mh = [( -gain(p, t), p, t ) for p, t in classes] # max-heap
        heapq.heapify(mh)

        for _ in range(extraStudents):

            g, p, t = heapq.heappop(mh)
            p += 1
            t += 1
            heapq.heappush(mh, (-gain(p, t), p, t))
        
        total_ratio = 0
        for g, p, t in mh:
            total_ratio += (p/t)
        
        return total_ratio / len(mh)
        

