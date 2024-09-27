from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        n = len(arr)
        result = 0
        minque = deque()

        for currentindex in range(n + 1):
            currentelement = 0 if currentindex == n else arr[currentindex]

            while minque and arr[minque[-1]] > currentelement:
                minelementindex = minque.pop()
                previousindex = -1 if not minque else minque[-1]

                # Count subarrays
                countsubarrays = (minelementindex  - previousindex)* (currentindex - minelementindex )
                result = (result + arr[minelementindex]*countsubarrays % MOD) % MOD
            minque.append(currentindex)

        return result % MOD
