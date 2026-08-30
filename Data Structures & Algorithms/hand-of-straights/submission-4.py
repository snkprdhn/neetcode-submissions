class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_len = len(hand)
        if hand_len%groupSize:
            return False
        
        
        hand_map = Counter(hand)
        h = list(hand_map.keys())
        heapq.heapify(h)

        while h:
            start = h[0]
            for num in range(start, start+groupSize):
                if hand_map[num]:
                    hand_map[num] -= 1
                    if not hand_map[num]:
                        if num != h[0]:
                            return False
                        heapq.heappop(h)
                else:
                    return False
                    
        return True

