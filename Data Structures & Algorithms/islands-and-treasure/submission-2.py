class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def get_negihbor(r,c):
            temp=[]
            if r+1 <len(grid): temp.append((r+1, c))
            if r-1>=0: temp.append((r-1, c))
            if c+1 <len(grid[0]): temp.append((r, c+1))
            if c-1 >=0: temp.append((r, c-1))
            return temp
        def bfs(R,C):
            q=deque()
            q.append((R, C))

            while q:
                R,C = q.popleft()
                for NR, NC in get_negihbor(R,C):
                    if grid[NR][NC] != -1 and grid[NR][NC] != 0:
                     
                        new_distance = grid[R][C]+1
                        if new_distance < grid[NR][NC]:
                            grid[NR][NC] = new_distance
                            q.append((NR, NC))
                        
            return grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    bfs(i,j)





        