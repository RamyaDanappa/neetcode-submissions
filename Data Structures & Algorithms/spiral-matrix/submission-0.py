class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row=len(matrix)
        col=len(matrix[0])
        direction=1
        i=0
        j=-1
        res=[]

        while row*col >0:
            for _ in range(col):
                j+=direction
                res.append(matrix[i][j])
            row-=1
            
            for _ in range(row):
                i+=direction
                res.append(matrix[i][j])
            col-=1
            direction*=-1
        return res
        