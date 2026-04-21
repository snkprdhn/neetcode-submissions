class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        max_freq = 0
        max_len = 0
        l = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r],0)+1
            max_freq = max(max_freq, cnt[s[r]])
            cur_len = r-l+1

            if cur_len - max_freq <= k:
                max_len = max(max_len, cur_len)
            else:
                cnt[s[l]]-=1
                l+=1
        return max_len
