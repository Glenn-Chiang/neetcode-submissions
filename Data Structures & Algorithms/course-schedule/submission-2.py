class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a graph where each course (node) points to its prerequisites (neighbors)
        # Graph is implemented as a hash map of node to neighbors
        graph = {}
        for course, prereq in prerequisites:
            graph[course] = graph.get(course, []) + [prereq]

        # DFS for cycle detection
        def dfs(course, path):
            # Cycle detected
            if course in path:
                return False
            
            # If course has no prerequisites, it is automatically finished
            if course not in graph:
                return True

            path.add(course)
            # Run DFS for each neighbor
            for prereq in graph[course]:
                if not dfs(prereq, path):
                    return False
            path.remove(course)

            # After we are done processing a course, mark it as done
            # by clearing its prerequisite list
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
        
        return True

