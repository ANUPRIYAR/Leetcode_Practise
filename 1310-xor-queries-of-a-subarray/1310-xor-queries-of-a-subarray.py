import math
class Query:
    def __init__(self, left, right, index):
        self.left = left
        self.right = right
        self.index = index

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        q = len(queries)

        prefix_xor = [0]* (n + 1)
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i-1] ^ arr[i-1]

        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])

        return result