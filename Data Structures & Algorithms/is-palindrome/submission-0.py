class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = []
        for c in s:
            if ord("a")<=ord(c)<=ord("z") or ord("A")<=ord(c)<=ord("Z") or ord("0")<=ord(c)<=ord("9"):
                new_str.append(c.lower())
        new_str = "".join(new_str)

        return new_str==new_str[::-1]
