import math
class Query:
    def __init__(self, left, right, index):
        self.left = left
        self.right = right
        self.index = index

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)

        blocksize = math.ceil(math.sqrt(n))

        queries = [Query(query[0], query[1], i) for i, query in enumerate(queries)]

        queries.sort(key = lambda q : (q.left//blocksize , q.right))

        currentleft, currentright = 0, -1
        min_difference = -math.inf
        count = [0]* 101

        ans = [0]* q
        for query in queries:
            left = query.left
            right = query.right

            while currentright < right:
                currentright += 1
                count[nums[currentright]] += 1

            while currentright > right:
                count[nums[currentright]] -= 1
                currentright -= 1
                
            while currentleft < left:
                count[nums[currentleft]] -= 1
                currentleft += 1

            while currentleft > left:
                currentleft -= 1
                count[nums[currentleft]] += 1

            currentdiff =  self.find_min_difference(count)
            ans[query.index] = currentdiff if currentdiff != math.inf else -1


        return ans

    def find_min_difference(self, count):
        min_diff = math.inf

        i = 0
        prev = -1
        while i < 101:
            if count[i] > 0:
                if prev != -1:
                    diff = abs(i - prev)
                    if diff < min_diff:
                        min_diff = diff
                prev = i
            i += 1
        
        return min_diff




        