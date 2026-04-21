class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        group_map = Counter(hand)
        h = list(group_map.keys())
        heapq.heapify(h)

        group_nums = n // groupSize
        for i in range(group_nums):
            num = h[0]
            group_map[num] -= 1
            if not group_map[num]:
                heapq.heappop(h)

            for j in range(groupSize-1):
                num+=1
                if not group_map[num]:
                    return False

                group_map[num] -= 1
                if not group_map[num]:
                    min_num = heapq.heappop(h)
                    if min_num != num:
                        return False
        return True