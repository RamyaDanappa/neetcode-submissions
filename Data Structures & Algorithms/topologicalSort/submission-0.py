class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        #build the adj List
        #indegree calculate

        indegree = [0]* n
        adj_list =defaultdict(list)
        for node, dependent in edges:
            
            adj_list[node].append(dependent)
            
            indegree[dependent]+=1
        
        q= deque()
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        res =[]
        while q:
            node= q.popleft()
            res.append(node)
            print(adj_list)
            for next_node in adj_list[node]:
                indegree[next_node]-=1
                if indegree[next_node]==0:
                    q.append(next_node)
        return res if len(res) == n else []
        