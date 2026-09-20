class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def get_neighbor(x, y):
            res = []
            if x - 1 >= 0:
                res.append((x - 1, y))
            if x + 1 < len(image):
                res.append((x + 1, y))
            if y - 1 >= 0:
                res.append((x, y - 1))
            if y + 1 < len(image[0]):
                res.append((x, y + 1))
            return res
        def bfs(r,c):
            start_color =image[sr][sc]
            if start_color== color:
                return
            q=deque()
            q.append((r,c))
            image[r][c]=color
            while q:
                r,c =q.popleft()
                next_neigbor=get_neighbor(r,c)
              
                for NR, NC in next_neigbor:
                    if image[NR][NC] == start_color :
                        image[NR][NC]= color
                        q.append((NR,NC))
        for i in range(len(image)):
            for j in range(len(image[0])):
                if i==sr and j ==sc:
                    bfs(i,j)
        return image
        