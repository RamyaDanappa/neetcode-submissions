class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[-1]*n
        adj_list= [[] for _ in range(n)]
        for (src, dest) in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        def bfs(source):
            visited[source]=1
            q=deque()
            q.append(source)
            while q:
                node=q.popleft()
                for neigbor in adj_list[node]:
                    if visited[neigbor] != 1:
                        visited[neigbor]=1
                        q.append(neigbor)
        count= 0
        for i in range(n):
            if visited[i] != 1:
                count+=1
                bfs(i)
        return count
        