class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        row = -1
        while l<=r:
            print(f"l:{l}, r:{r}")
            idx = l + ((r-l)//2)
            print(f"idx:{idx}")
            if matrix[idx][0] > target:
                r = idx - 1
            elif matrix[idx][-1] < target:
                l = idx + 1
            else:
                row = idx
                break
        
        print(row)
        if row != -1:
            l = 0;
            r = len(matrix[0])-1
            while l<=r:
                idx = l + ((r-l)//2)
                if matrix[row][idx]<target:
                    l = idx+1
                elif matrix[row][idx]>target:
                    r = idx-1
                else:
                    return True
        
        return False