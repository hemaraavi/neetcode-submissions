class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        n = len(matrix[0]) -1
        while l<=r:
            m = l+(r-l)//2
            if matrix[m][0]<= target and matrix[m][n] >= target:
                if target in matrix[m] :
                    return True
                else:
                    return False
            elif matrix[m][0]> target:
                r = m-1
            else:
                l= m+1
        return False