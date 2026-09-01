class Solution:

    def encode(self, strs: List[str]) -> str:
        # len of str + str
        def get_digits(num):
            cnt = 0
            while num:
                cnt += 1
                num //= 10
            return cnt

        res = ""
        for word in strs:
            n = len(word)
            res += str(get_digits(n))
            if n:
                res += str(n)
                res += word
        
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        #print(s)
        res = []
        digits = int(s[0])
        cnt = 0
        word = ""
        for ch in s[1:]:
            #print(ch, cnt, word, res)
            if digits:
                cnt *= 10
                cnt += int(ch)
                digits -= 1
            elif cnt:
                word += ch
                cnt -= 1
            else:
                res.append(word)
                word = ""
                digits = int(ch)
        res.append(word)
        
        return res
            