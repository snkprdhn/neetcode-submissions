class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        
        if "0000" in deadends:
            return -1
        
        visited = set(deadends)
        q = deque(["0000"])
        visited.add("0000")

        steps = 0

        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return steps

                for i in range(4):
                    new_lock_up = lock[:i] + str((int(lock[i])+1)%10) + lock[i+1:]
                    new_lock_down = lock[:i] + str((int(lock[i])-1+10)%10) + lock[i+1:]

                    if new_lock_up not in visited:
                        q.append(new_lock_up)
                        visited.add(new_lock_up)
                    
                    if new_lock_down not in visited:
                        q.append(new_lock_down)
                        visited.add(new_lock_down)
            steps += 1
            
        return -1
