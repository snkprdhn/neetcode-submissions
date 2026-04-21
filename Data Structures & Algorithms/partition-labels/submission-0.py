class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_map = {}
        n = len(s)
        for i in range(n):
            char_map[s[i]] = i
        
        size = end = 0
        res = []
        for i in range(n):
            end = max(end, char_map[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res