class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        
        for num in reversed(nums2):
            
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                hashmap[num] = stack[-1]
            
            stack.append(num)

        answer = []
        for query in nums1:
            answer.append(hashmap.get(query, -1))

        return answer






        