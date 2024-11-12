from heapq import heappush , heappop
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        maxheap = []
        answer = [0]* len(queries)
        items.sort(key = lambda x:(x[0] , x[1]))
        for i, query in enumerate(queries):
            for price , beauty in items:
                if price <= query:
                    heappush(maxheap, (-beauty , price))
            if maxheap:
                b, p = heappop(maxheap)
                answer[i] = -b
            # print(max_beauty)
            # answer.append(max_beauty)

        return answer
            


        
        