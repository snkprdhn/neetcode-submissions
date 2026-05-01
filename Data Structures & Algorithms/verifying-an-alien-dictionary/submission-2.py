class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = defaultdict(int)
        for i in range(len(order)):
            if order[i] not in order_index:
                order_index[order[i]] = i

        n = len(words)
        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]

            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return False
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False      
                    break
        
        return True
