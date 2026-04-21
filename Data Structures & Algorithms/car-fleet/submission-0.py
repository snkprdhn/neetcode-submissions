class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s_pair = [[p,s] for p, s in zip(position, speed)]
        p_s_pair.sort()
        print(p_s_pair)
        time_to_reach = []
        for p, s in p_s_pair:
            time_to_reach.append((target-p)/s)

        # [3, 8]

        s = []
        print(time_to_reach)
        for t in time_to_reach:
            while s and s[-1] <= t:
                s.pop()
            s.append(t)
        
        print(s)
        return len(s)