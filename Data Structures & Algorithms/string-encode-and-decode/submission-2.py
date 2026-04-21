class Solution:

    def encode(self, strs: List[str]) -> str:
        if not len(strs):
            return "$$"
        res = ""
        for st in strs:
            res+= f"{len(st)}${st}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        if s == "$$":
            return []
        res = []
        cur_str = ""
        len_cur_str = 0
        start_str = False
        reached_deli = False
        for i in range(0,len(s)):
            print((ord("0")<=ord(s[i])<=ord("9")), not start_str)
            if (ord("0")<=ord(s[i])<=ord("9")) and not start_str:
                start_str = True
                len_cur_str = ord(s[i]) - ord("0")
            elif (ord("0")<=ord(s[i])<=ord("9")) and not reached_deli:
                len_cur_str *= 10
                len_cur_str += ord(s[i]) - ord("0")
            elif s[i]=="$" and not reached_deli:
                reached_deli = True
            elif not len_cur_str:
                res.append(cur_str)
                start_str = True
                reached_deli = False
                cur_str = ""
                len_cur_str = ord(s[i]) - ord("0")
            else:
                len_cur_str -= 1
                cur_str += s[i]
            print(f"i={i}, s[i]={s[i]}, cur_str={cur_str}, res={res}, start_str={start_str}, reached_deli={reached_deli}, len_cur_str={len_cur_str}")

        res.append(cur_str)
        return res
            

            
