class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def get_neighbor(x,y):
            res = []
            if x - 1 >= 0:
                res.append((x - 1, y))
            if x + 1 < len(grid):
                res.append((x + 1, y))
            if y - 1 >= 0:
                res.append((x, y - 1))
            if y + 1 < len(grid[0]):
                res.append((x, y + 1))
            return res
        def bfs(r,c):
            q= deque()
            count=1
            q.append((r,c))
            grid[r][c]=0
            while q:
                r,c  =q.popleft()
                for NR, NC in get_neighbor(r,c):
                    if grid[NR][NC] == 1:
                    
                        count+=1
                        grid[NR][NC]=0
                        q.append((NR,NC))
            
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    
                    count =bfs(i,j)
                    max_area=max(max_area,count)
        return max_area
