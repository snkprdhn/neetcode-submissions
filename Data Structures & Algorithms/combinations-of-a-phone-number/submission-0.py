class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res, sol = [],[]

        res, sol = [],[]
        n = len(digits)

        def backtrack(i):
            if i==n:
                if sol:
                    res.append("".join(sol[:]))
                return
            
            for char in dig_map[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return res