class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]* numCourses
        adj_lsit=[[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course]+=1
            adj_lsit[prereq].append(course)
        
        q=deque()
        for course in range(numCourses):
            if indegree[course]==0:
                q.append(course)
        finish=0
        while q:
            curr_course = q.popleft()
            finish+=1

            for next_course in adj_lsit[curr_course]:
                indegree[next_course]-=1
                if indegree[next_course]==0:
                    q.append(next_course)
        if finish == numCourses:
            return True
        else:
            return False

        