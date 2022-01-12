class Solution:
    def findOrder(self, numCourses, preprequisites):
        in_degree_table = {}
        for i in range(numCourses):
            in_degree_table[i] = 0

        edges = {}

        for course_second, course_first in preprequisites:
            if course_first not in edges:
                edges[course_first] = []
            edges[course_first].append(course_second)
            in_degree_table[course_second] += 1

        orders = []
        queue = []

        # get course whose in degree == 0
        for course, in_degree in in_degree_table.items():
            if in_degree == 0:
                queue.append(course)

        # traversal queue
        while not queue:
            course = queue.pop(0)
            orders.append(course)
            numCourses -= 1
            for target_course in edges[course]:
                in_degree_table[target_course] -= 1
                if in_degree_table[target_course] == 0:
                    queue.append(target_course)

        if numCourses > 0:
            return []

        return orders



