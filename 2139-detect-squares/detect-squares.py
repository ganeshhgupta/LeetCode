class DetectSquares:

    # O(1), O(1)

    def __init__(self):
        self.squares = defaultdict(int)

    # O(1), O(1)

    def add(self, point: List[int]) -> None:
        self.squares[tuple(point)] += 1

    # O(n), O(1)

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point

        for (x, y), count in self.squares.items():
            if abs(py - y) == abs(px - x) and (py != y and px != x):

                result += count * self.squares.get((x, py), 0) * self.squares.get((px, y), 0)
        return result