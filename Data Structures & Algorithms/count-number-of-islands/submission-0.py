class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbor(x,y):
            temp=[]
            if x+1 <len(grid):
                temp.append((x+1, y))
            if y+1 <len(grid[0]):
                temp.append((x,y+1))
            if x-1>=0:
                temp.append((x-1, y))
            if y-1>=0:
                temp.append((x,y-1))
            return temp
                
        def bfs(i,j):
            q=deque()
            q.append((i,j))
            grid[i][j]="0"
            while q:
                (r,c)=q.popleft()
                node_neighbor=get_neighbor(r,c)
                for R,C in node_neighbor:
                    if grid[R][C] !="0":
                        q.append((R,C))
                        grid[R][C]="0"
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!="0":
                    bfs(i,j)
                    count+=1
        return count
                
        