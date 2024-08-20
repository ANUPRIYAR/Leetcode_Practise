from heapq import heappush
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # store index of the order in which tasks are processed
        # we have to execute a task only after its start time. if there are mutiple tasks
        # which are below the current time, then we have to excute tasks with smallest RTO


        # add index, for tracking 
        for i, t in enumerate(tasks):
            tasks[i].append(i)

        # sort based on start time 
        tasks.sort(key = lambda x: x[0])

        result = []
        minheap = []

        i, time = 0, tasks[0][0]

        while minheap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(minheap, (tasks[i][1], tasks[i][2]))
                i += 1

            if minheap:
                proctime, index = heappop(minheap)
                time += proctime
                result.append(index)
            else:
                time = tasks[i][0]

        return result

   
        



        