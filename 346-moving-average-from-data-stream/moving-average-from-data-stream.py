class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum  -= self.q.popleft()        
        return self.sum/len(self.q)