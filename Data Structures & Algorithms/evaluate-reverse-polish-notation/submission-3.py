class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        op = ["+","-","*","/"]
        for t in tokens:
            if t == "+":
                s.append(s.pop() + s.pop())
            elif t == "-":
                a, b = s.pop(), s.pop()
                s.append(b - a)
            elif t == "*":
                s.append(s.pop() * s.pop())
            elif t == "/":
                a, b = s.pop(), s.pop()
                s.append(int(b/a))
            else:
                s.append(int(t))
        return s.pop()