class Solution:
    def find_palin(self, l, r, s):
        n = len(s)
        while l >= 0 and r < n and s[l]==s[r]:
            if (r-l+1)>self.max_len:
                self.max_len = r-l+1
                self.res = s[l:r+1]
            l-=1
            r+=1

    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.max_len = 0

        for i in range(len(s)):
            # odd length
            l = r = i
            self.find_palin(l,r, s)
            
            # even length
            l, r = i, i+1
            self.find_palin(l,r, s)
        
        return self.res
