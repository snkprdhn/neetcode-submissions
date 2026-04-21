class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1

        while l <= r and t <= b:   # ✅ fix 1
            # print tl->tr
            for i in range(l, r + 1):   # ✅ fix 2
                res.append(matrix[t][i])
            
            # print tr->br
            for i in range(t + 1, b + 1):   # ✅ fix 3
                res.append(matrix[i][r])

            if t < b:   # ✅ fix 4
                # print br->bl
                for i in range(r - 1, l - 1, -1):   # ✅ fix 5
                    res.append(matrix[b][i])

            if l < r:   # ✅ fix 6
                # print bl->tl
                for i in range(b - 1, t, -1):   # ✅ fix 7
                    res.append(matrix[i][l])
            
            l += 1
            r -= 1
            t += 1
            b -= 1
        
        return res