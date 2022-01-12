
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """
            1
        0      3
            2
        """

        if numCourses == 0 or len(prerequisites) == 0:
            return True
        # in degree
        course_table = {}
        neighbors_table = {}
        for course in range(numCourses):
            course_table[course] = 0
            neighbors_table[course] = []
        for course in prerequisites:
            target, source = course[0], course[1]
            course_table[target] += 1
            neighbors_table[source].append(target)

        # queue
        queue = []
        for course, in_degree in course_table.items():
            if in_degree == 0:
                queue.append(course)

        while queue != []:
            course = queue.pop(0)
            numCourses -= 1
            for target in neighbors_table[course]:
                course_table[target] -= 1  # in degree minus 1
                if course_table[target] == 0:
                    queue.append(target)

        return numCourses == 0