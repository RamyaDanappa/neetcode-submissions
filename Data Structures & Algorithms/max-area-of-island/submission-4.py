class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def get_neigbour(x,y):
            res = []
            if x+1<len(grid): res.append((x+1,y))
            if x-1>=0: res.append((x-1, y))
            if y+1<len(grid[0]): res.append((x, y+1))
            if y-1>=0:res.append((x, y-1))
            return res
        def bfs(R,C):
            
            q=deque()
            q.append((R,C))
            count=1
            grid[R][C]=0
            while q:
                R,C = q.popleft()
                for (NR, NC) in get_neigbour(R,C):
                    if grid[NR][NC] == 1:
                        grid[NR][NC]=0
                        count+=1
                        q.append((NR,NC))
            return count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    val = bfs(i,j)
                    max_area= max(max_area, val)
        return max_area