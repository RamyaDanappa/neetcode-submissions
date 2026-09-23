class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res =[]
        indegree=[0]*numCourses
        adj_list=[[] for _ in range(numCourses)]

        for course,prereq in prerequisites:
            indegree[course]+=1
            adj_list[prereq].append(course)
        q=deque()

        for course in range(numCourses):
            if indegree[course]==0:
                q.append(course)
        finish=0
        while q:
            curr_course = q.popleft()
            res.append(curr_course)
            finish +=1

            for next_course in adj_list[curr_course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    q.append(next_course)
        
        if finish == numCourses:return res
        else: return []