class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        # Build graph
        for course, prerequisite in prerequisites:
            indegree[course] += 1
            adj_list[prerequisite].append(course)

        # Courses with no prerequisites
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        # Process courses
        finish = 0

        while q:
            course = q.popleft()
            finish += 1

            for next_course in adj_list[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        # If we processed every course, there is no cycle
        if finish == numCourses:
            return True
        else:
            return False