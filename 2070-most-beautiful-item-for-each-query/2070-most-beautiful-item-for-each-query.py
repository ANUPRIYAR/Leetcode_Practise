class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        stack = [(0, 0)]
        items.sort(key = lambda x:(x[0], x[1]))
        for price, beauty in items:
            if price == stack[-1][0] and beauty > stack[-1][1]:
                stack.pop()
                stack.append((price, beauty))
            elif beauty > stack[-1][1]:
                stack.append((price, beauty))
        print(stack)
        answer = [0]*len(queries)
        for i, query in enumerate(queries):
            beauty = self.binary_search(stack, query)
            
            answer[i] = beauty

        return answer
            

    def binary_search(self, array, target):
        left = 0
        right = len(array) - 1
        lower_value = None

        while left <= right:
            mid = left + (right - left)//2
            if array[mid][0] < target:
                lower_value = array[mid][1]
                left = mid + 1
            elif array[mid][0] > target:
                right = mid - 1
            else:
                return array[mid][1]

        return lower_value




        