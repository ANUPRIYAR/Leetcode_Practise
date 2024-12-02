class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]* numCourses
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1


        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)


        topo_sort = []
        while queue:
            node = queue.popleft()
            topo_sort.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)


        if len(topo_sort) < numCourses:
            return False

        return True




        

        