class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t=="":
            return ""

        cnt_t = {}
        window = {}
        for ch in t:
            cnt_t[ch] = cnt_t.get(ch, 0) + 1

        cnt_s = {}
        have, need = 0, len(cnt_t)
        res, res_len = [-1,-1], float("infinity")

        l = 0 
        for r in range(len(s)):   
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t and window[c]==cnt_t[c]:
                have += 1
            
            while have == need:
                cur_len = r-l+1
                if cur_len < res_len:
                    res_len = cur_len
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in cnt_t and window[s[l]] < cnt_t[s[l]]:
                    have -= 1
                l += 1
            
        
        l, r = res
        return s[l:r+1] if res_len!=float("infinity") else ""
                
                