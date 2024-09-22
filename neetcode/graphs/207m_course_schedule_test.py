import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre_map = collections.defaultdict(list)
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        visit_set = set()

        def dfs(course):
            if course in visit_set:
                return False
            if pre_map[course] == []:
                return True

            visit_set.add(course)
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            visit_set.remove(course)
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
