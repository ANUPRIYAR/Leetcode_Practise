class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_xor[i] ^= prefix_xor[i-1] ^ nums[i]

        print(prefix_xor)
        curxor = 0
        k = len(nums)
        answer = []
        while k > 0:
            curxor = prefix_xor[k-1]

            allsetbits = (1<< maximumBit) - 1
            answer.append(curxor ^ allsetbits)
            k -= 1


        return answer
            

        

        