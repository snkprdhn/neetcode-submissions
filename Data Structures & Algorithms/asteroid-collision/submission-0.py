class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for ast in asteroids:
            if ast>0:
                res.append(ast)
            else:
                ast *= -1
                while res and res[-1]>0 and res[-1]<ast:
                    res.pop()
                if res and res[-1]==ast:
                    res.pop()
                elif not res or res[-1]<0:
                    res.append(-ast)
        return res
