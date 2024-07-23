class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # check if unset but if n is also unset for k
        if n == k :
            return 0

        count = 0
        while n > 0 or  k >0 :
            if n & 1 == 1 and k & 1 == 0:
                count += 1
            if n & 1 == 0 and k & 1 == 1:
                return -1

            n >>= 1
            k >>= 1

        return count