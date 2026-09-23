class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res =[]
        indegree =[0]*numCourses
        adj_list=[[] for _ in range(numCourses)]

        for src, dest in prerequisites:
            indegree[dest]+=1
            adj_list[src].append(dest)
        
        q=deque()
        for n in range(numCourses):
            if indegree[n]==0:
                q.append(n)
        finish =0
        while q:
            course = q.popleft()
            finish+=1
            res.append(course)

            for next_course in adj_list[course]:
                indegree[next_course]-=1
                if indegree[next_course] ==0:
                    q.append(next_course)
        if finish== numCourses:
            return res[::-1]
        else:
            return []

        
        