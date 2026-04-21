class Solution:
    def numDecodings(self, s: str) -> int:
        # split into sub numbers less than 27 without any leading 0s
        n = len(s)
        next1 = 1
        next2 = 0

        for i in range(n-1,-1,-1):
            if s[i]=="0":
                cur = 0
            else:
                cur = next1
                if i+1 < n and int(s[i:i+2]) <= 26:
                    cur += next2
            next1, next2 = cur, next1

        return next1