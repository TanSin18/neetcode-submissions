class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        top,bottom=0,r-1
        while bottom>=top:
            row=int((top+bottom)/2)
            if target<matrix[row][0]:
                bottom=row-1
            elif target>matrix[row][-1]:
                top=row+1
            else:
                break
        if not(bottom>=top):
            return False

        row=int((top+bottom)/2)
        l,r=0,c-1
        while r>=l:
            col=int((l+r)/2)
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                r=col-1
            elif target>matrix[row][col]:
                l=col+1
            else:
                False
        return False
