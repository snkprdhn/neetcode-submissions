class Solution:
    def isValid(self, s: str) -> bool:
        q = collections.deque()
        p_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        for p in s:
            if p in p_map:
                if not q or q[-1] != p_map[p]:
                    return False
                else:
                    q.pop()
            else:
                q.append(p)
        
        if q:
            return False
        return True