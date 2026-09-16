class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res =[]
        if not matrix:
            return res 
        
        row=len(matrix)
        col=len(matrix[0])
        i,j=0,-1
        direction=1
        while row*col>0:
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