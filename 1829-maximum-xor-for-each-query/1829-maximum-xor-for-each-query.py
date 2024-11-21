class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        q = len(nums)
        query = [-1]* q
        prefix_xor, index = 0, 0

        # Calculating prefix_xor in advance
        prefix_xor = 0
        for num in nums:
            prefix_xor ^= num

        while q > 0:
            all_ones = (1 << maximumBit) - 1  #allones of given bitlength will be max number
            query[index] = prefix_xor ^ all_ones  # xoring allones with current xor will give k
            num = nums.pop()  # popping last element
            prefix_xor ^= num     # and removing the contribution of popped element
            
            q-= 1
            index += 1
            
        return query 