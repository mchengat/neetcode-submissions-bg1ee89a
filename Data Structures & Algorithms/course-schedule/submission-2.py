class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return taken == numCourses