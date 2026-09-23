class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        adj_list=[[] for _ in range(numCourses)]
        for src,dest in prerequisites:
            indegree[dest]+=1
            adj_list[src].append(dest)
        
        q=deque()
        for n in range(numCourses):
            if indegree[n]==0:
                q.append(n)
        finish=0
        while q:
            course=q.popleft()
            finish+=1

            for next_course in adj_list[course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    q.append(next_course)
        
        if finish==numCourses:
            return True
        else:
            return False

        