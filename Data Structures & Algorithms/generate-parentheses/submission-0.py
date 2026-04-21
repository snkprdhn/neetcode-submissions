class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(i, open_p, close_p):
            if open_p == close_p == n:
                res.append("".join(sol[:]))
                return

            if open_p > close_p:
                # add open or close
                if open_p < n:
                    sol.append("(")
                    open_p += 1
                    backtrack(i+1, open_p, close_p)
                    sol.pop()
                    open_p -= 1

                sol.append(")")
                close_p += 1
                backtrack(i+1, open_p, close_p)
                sol.pop() 
                close_p -= 1              
            elif open_p == close_p:
                # add open
                sol.append("(")
                open_p += 1
                backtrack(i+1, open_p, close_p)
                sol.pop()
                open_p -= 1

        
        backtrack(0, 0, 0)
        return res
