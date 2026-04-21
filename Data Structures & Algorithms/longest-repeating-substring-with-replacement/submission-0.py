class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        max_freq = 0
        max_len = 0
        l = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r],0)+1
            max_freq = max(max_freq, cnt[s[r]])
            len_r = (r-l+1)

            if len_r - max_freq <= k:
                max_len = max(max_len, len_r)
            else:
                cnt[s[l]]-=1
                l+=1
        return max_len
