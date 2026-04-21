class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1 if x >= 0 else -1
        x = abs(x)

        res = 0
        while x:
            digit = x % 10
            x = x // 10

            if (res > INT_MAX//10) or (res == INT_MAX//10 and digit>INT_MAX%10):
                return 0
            
            res = res * 10
            res = res + digit
        
        return sign*res if INT_MIN <= res <= INT_MAX else 0