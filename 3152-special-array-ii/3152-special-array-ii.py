class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        group = 0
        check = []
        check.append(group)
        for i in range(1,len(nums)):
            if self.parity(nums[i-1]) == self.parity(nums[i]):
                group += 1

            check.append(group)
        
        answer = []
        for start, end in queries:
            if check[start] == check[end]:
                answer.append(True)
            else:
                answer.append(False)

        return answer


        




        



    def parity(self, num):
        return num % 2 == 0