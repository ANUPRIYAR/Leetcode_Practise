class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = rsum = 0
        maxsum = 0

        rindex = len(cardPoints) - 1

        for i in range(k):
            lsum += cardPoints[i]


        maxsum = lsum
        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            rindex -= 1
            maxsum = max(maxsum, lsum + rsum)

        return maxsum

        


        