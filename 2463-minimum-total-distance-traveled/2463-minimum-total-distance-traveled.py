class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        rcount, fcount = len(robot), len(factory)

        # dp table creation
        dp = [[0]* (fcount+1) for _ in range(rcount + 1)]

        for i in range(rcount):
            dp[i][-1] = float('inf')

        for j in range(fcount-1, -1, -1):
            prefix = 0
            qq = deque([(rcount, 0)])

            # Inner loop: process each robot right to left
            for i in range(rcount-1, -1, -1):
                # cumulative distance for current robot to factory
                prefix += abs(robot[i] - factory[j][0])

                if qq[0][0] > i + factory[j][1]:
                    qq.popleft()

                while qq and qq[-1][1] >= dp[i][j+1] - prefix:
                    qq.pop()

                qq.append((i, dp[i][j+1] - prefix))
                dp[i][j] = qq[0][1] + prefix

        return dp[0][0]

        




        