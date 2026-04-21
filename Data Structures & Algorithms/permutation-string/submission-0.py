class Solution:
    def checkSame(self, cnt_s1, cnt_s2):
        for key, val in cnt_s1.items():
            if (key not in cnt_s2) or cnt_s2[key]!=val:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = {}
        cnt_s2 = {}

        for c in s1:
            cnt_s1[c] = cnt_s1.get(c, 0)+1

        if len(s1)>len(s2):
            return False

        l = 0
        for r in range(len(s2)):
            cnt_s2[s2[r]] = cnt_s2.get(s2[r], 0)+1
            cur_len = r-l+1

            if cur_len==len(s1):
                if self.checkSame(cnt_s1, cnt_s2):
                    return True
                else:
                    cnt_s2[s2[l]]-=1
                    l+=1

        return False
