class Solution:
    def find_palin(self, s, l, r):
        n = len(s)
        palin_sub_strings = 0
        while l >= 0 and r < n and s[l] == s[r]:
            palin_sub_strings += 1
            l-=1
            r+=1

        return palin_sub_strings

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_palin_sub_strings = 0
        for i in range(n):
            total_palin_sub_strings += self.find_palin(s,i,i)
            total_palin_sub_strings += self.find_palin(s,i,i+1)
        
        return total_palin_sub_strings