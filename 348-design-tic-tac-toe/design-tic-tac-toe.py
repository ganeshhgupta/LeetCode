class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.r = [0] * n   # rows
        self.c = [0] * n   # cols
        self.d = 0         # main diagonal
        self.a = 0         # anti diagonal

    def move(self, row: int, col: int, p: int) -> int:
        v = 1 if p == 1 else -1

        self.r[row] += v
        self.c[col] += v

        if row == col:
            self.d += v

        if col == self.n - 1 - row:
            self.a += v

        if (abs(self.r[row]) == self.n or
            abs(self.c[col]) == self.n or
            abs(self.d) == self.n or
            abs(self.a) == self.n):
            return p
        return 0
