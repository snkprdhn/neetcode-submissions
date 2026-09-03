class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        days = 1
        while self.s and self.s[-1][0]<=price:
            days += self.s[-1][1]
            self.s.pop()
        
        self.s.append((price, days))
        return days
