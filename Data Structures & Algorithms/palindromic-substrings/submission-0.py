class Solution:
    def find_palin(self, l, r, s):
        n = len(s)
        max_len = 0
        palin_sub_strings = 0
        while l >= 0 and r < n and s[l] == s[r]:
            cur_len = r-l+1
            if cur_len > max_len:
                max_len = cur_len
                palin_sub_strings += 1
            l-=1
            r+=1
            
        return palin_sub_strings

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_palin_sub_strings = 0
        for i in range(n):
            l=r=i
            total_palin_sub_strings += self.find_palin(l,r,s)

            l,r = i, i+1
            total_palin_sub_strings += self.find_palin(l,r,s)
        
        return total_palin_sub_strings