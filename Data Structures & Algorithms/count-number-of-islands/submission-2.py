class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
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

            while q:
                R,C = q.popleft()
                for (NR, NC) in get_neigbour(R,C):
                    if grid[NR][NC] == "1":
                        grid[NR][NC]="0"
                        q.append((NR,NC))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    count+=1
                    bfs(i,j)
                
        return count
        