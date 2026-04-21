class Solution:
    def checkSame(self, cnt_s1, cnt_s2):
        for i in range(len(cnt_s1)):
            if cnt_s1[i]!=cnt_s2[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt_s1 = [0]*26
        cnt_s2 = [0]*26

        for c in s1:
            cnt_s1[ord(c)-ord('a')] += 1

        if len(s1)>len(s2):
            return False

        l = 0
        for r in range(len(s2)):
            cnt_s2[ord(s2[r]) - ord('a')] += 1
            cur_len = r-l+1

            if cur_len==len(s1):
                if self.checkSame(cnt_s1, cnt_s2):
                    return True
                else:
                    cnt_s2[ord(s2[l])-ord('a')]-=1
                    l+=1

        return False
