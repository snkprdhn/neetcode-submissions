class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        tasks = [-cnt for cnt in c.values()]
        heapq.heapify(tasks)

        q = deque()
        time = 0
        while tasks or q:
            time+=1
            if tasks:
                cnt = 1 + heapq.heappop(tasks)
                if cnt:
                    q.append([cnt, time+n])
            else:
                time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(tasks, q.popleft()[0])
        return time
