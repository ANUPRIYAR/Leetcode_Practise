class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1 
        freq = Counter(nums)
        operations = len(freq) - 1 if k in nums else len(freq)
        return operations




        
                    
        