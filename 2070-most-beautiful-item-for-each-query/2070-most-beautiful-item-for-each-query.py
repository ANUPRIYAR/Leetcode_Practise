from heapq import heappush , heappop
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        bucket = [[0, 0, 9999]]
        items.sort(key=lambda x:(x[0], x[1]))
        for price, beauty in items:
            print(beauty,bucket[-1][1] )
            if price == bucket[-1][0] and beauty > bucket[-1][1]:
                bucket[-1][1] = beauty
            elif beauty > bucket[-1][1]:
                bucket.append([price, beauty, price])
        print(bucket)

        answer = []
        for query in queries:
            index = self.binary_search(bucket, query)
            answer.append(bucket[index][1])

        return answer

            
                
    def binary_search(self, bucket, query):
        left, right = 0, len(bucket) - 1

        while left <= right:
            mid = left + (right - left)//2

            if bucket[mid][0] < query:
                lower_index = mid
                left = mid + 1
            elif bucket[mid][0] > query:
                right = mid -1 
            else:
                return mid

        return lower_index

       
