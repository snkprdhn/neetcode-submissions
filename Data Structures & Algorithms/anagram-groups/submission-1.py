class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an_map = defaultdict(list)
        for st in strs:
            cnt = [0]*26
            for ch in st:
                cnt[ord(ch)-ord('a')]+=1
            an_map[tuple(cnt)].append(st)
        
        res = []
        for st in an_map.values():
            res.append(st)
        return res