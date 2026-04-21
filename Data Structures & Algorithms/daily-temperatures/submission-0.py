class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        q = collections.deque()
        for r in range(len(temperatures)):
            num = temperatures[r]
            while q and num > temperatures[q[-1]]:
                res[q[-1]] = r - q[-1]
                q.pop()
            q.append(r)
        return res