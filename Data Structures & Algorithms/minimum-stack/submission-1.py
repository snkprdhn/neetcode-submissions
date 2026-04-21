class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if self.s:
            min_s = min(self.s[-1][1], val)
        else:
            min_s = val
        self.s.append([val,min_s])

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]

-2 , 0 , -3