class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        # 0 = not visited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            state[course] = 2
            return True

        return all(dfs(course) for course in range(numCourses))