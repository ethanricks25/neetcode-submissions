from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        q = deque()

        for course, prereq in prerequisites:
            graph[course].append(prereq)
            indegree[prereq] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        while q:
            course = q.popleft()
            finish += 1
            for prereq in graph[course]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)
        return finish == numCourses