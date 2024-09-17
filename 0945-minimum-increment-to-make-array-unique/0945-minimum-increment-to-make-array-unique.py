class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0
        min_moves = 0

        # find the maximum value in the array
        max_val = max(nums)

        # Create a frequency array to count occurences
        freq = [0]* (n + max_val + 1)

        # Populate frequency array
        for value in nums:
            freq[value] += 1

        moves = 0
        # Adjust freqeuncyies to make all value unique
        for i in range(len(freq)):
            if freq[i] <= 1:
                continue

            excess = freq[i] - 1
            freq[i + 1] += excess
            moves += excess

        return moves
            