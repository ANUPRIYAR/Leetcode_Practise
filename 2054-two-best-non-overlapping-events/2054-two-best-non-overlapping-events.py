class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x:x[1])

        result = 0
        max_value  = 0

        max_until = []
        end_times = []

        for start, end , value in events:
            index = bisect.bisect_left(end_times, start) - 1
            max_previous = max_until[index] if index >= 0 else 0

            result = max(result, value + max_previous)

            max_value = max(max_value, value)
            max_until.append(max_value)
            end_times.append(end)

        return result


        