class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) -1

        while l < r:
            for i in range(r-l):
                t, b = l, r

                top_left = matrix[t][l+i]

                top_right = matrix[t+i][r]
                matrix[t+i][r] = top_left

                bot_right = matrix[b][r-i]
                matrix[b][r-i] = top_right

                bot_left = matrix[b-i][l]
                matrix[b-i][l] = bot_right

                matrix[t][l+i] = bot_left
            l += 1
            r -= 1