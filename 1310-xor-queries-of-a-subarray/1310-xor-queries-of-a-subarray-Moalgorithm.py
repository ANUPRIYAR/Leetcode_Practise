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

        blocksize = math.ceil(math.sqrt(n))
        answer = [0]*q

        queries = [Query(query[0],query[1], i)  for i, query in enumerate(queries)]
        queries.sort(key = lambda q:(q.left//blocksize, q.right))

        currentleft, currentright = 0, -1
        currentxor = 0 

        for  query in queries:
            left = query.left
            right = query.right


            while currentright < right:
                currentright += 1
                currentxor ^= arr[currentright]

            while currentright > right:
                currentxor ^= arr[currentright]
                currentright -= 1

            while currentleft > left:
                currentleft -= 1
                currentxor ^= arr[currentleft]
                

            while currentleft < left:
                currentxor ^= arr[currentleft]
                currentleft += 1
                
            answer[query.index] = currentxor

        return answer
            


        