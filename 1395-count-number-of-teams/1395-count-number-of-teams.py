class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0

        # @cache
        def backtrack(index, current):
            nonlocal count

            if len(current) == 3:
                if (current[0] < current[1] < current[2]) or (current[0] > current[1] > current[2]):
                    count += 1
                return 
                # return False

            for i in range(index, len(rating)):
                current.append(rating[i])
                backtrack(i + 1, current)
                current.pop()

            return count


        backtrack(0, [])
        return count




        