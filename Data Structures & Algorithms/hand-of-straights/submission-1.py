class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        group_map = Counter(hand)
        h = list(group_map.keys())
        heapq.heapify(h)

        while h:
            start = h[0]

            for num in range(start, start+groupSize):
                if not group_map[num]:
                    return False
                
                group_map[num] -= 1

                if not group_map[num]:
                    if num != h[0]:
                        return False
                    heapq.heappop(h)
        
        return True