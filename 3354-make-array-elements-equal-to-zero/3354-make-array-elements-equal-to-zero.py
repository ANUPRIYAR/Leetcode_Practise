class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n  = len(nums)

        count = 0
        arr = nums.copy()
        
        for i in range(len(nums)):
            if nums[i] == 0:
                arr = nums.copy()
                if self.simulation(arr, i, left=True):
                    count += 1

                arr = nums.copy()
                if self.simulation(arr, i, left=False):
                    count += 1

        return count

    def simulation(self, array, curr, left=False):
            n = len(array)
            i = curr
            while i >= 0 and i < n:
                if array[i] == 0:
                    if left:
                        i -= 1
                    else:
                        i += 1
                elif array[i] > 0:
                    array[i] -= 1
                    if left :
                        i += 1
                        left = False
                    else:
                        i -= 1
                        left = True 
            return len(set(array)) == 1 and 0 in array
            

            


                    
                    
            
                    
                
        