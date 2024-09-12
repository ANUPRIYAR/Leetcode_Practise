class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        nstart, nend =  newInterval[0], newInterval[1]
        n = len(intervals)
        i = 0
        res = []
        while i < n and intervals[i][1] < nstart:
            res.append(intervals[i])
            i += 1
            print(i)

        # overlapping because we already covered (s < nend where e < nend) in the above, so we are only left s < nend where e is not smaller than nend, thus #overlapping
        while i < n and intervals[i][0] <= nend: 
            nstart = min(intervals[i][0], nstart)
            nend =  max(intervals[i][1], nend)
            i += 1

        res.append([nstart, nend])

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
