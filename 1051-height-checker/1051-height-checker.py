class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        max_val = max(heights)
        count = [0]* (max_val + 1)

        for height in heights:
            count[height] += 1

        # cumulative frequency
        for i in range(1, len(count)):
            count[i] += count[i-1]


        expected = [0]* len(heights)

        for i in range(len(heights)):
            expected[count[heights[i]] - 1] = heights[i]
            count[heights[i]] -= 1

        # Compare expected and heights
        non_match = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                non_match += 1


        return non_match





        