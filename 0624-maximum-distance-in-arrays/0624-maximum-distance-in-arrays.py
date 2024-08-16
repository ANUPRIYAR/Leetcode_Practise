class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort()
        print(arrays)
        smallest1, smallest2 = math.inf, math.inf
        largest1, largest2 = 0, 0

        small_index1 = large_index1 = large_index2 =small_index2 = math.inf

        for i in range(len(arrays)):
            if arrays[i][0]< smallest1:
                smallest1 = arrays[i][0]
                small_index1 = i

        print(f"smallest1 : {smallest1 }")

        for j in range(len(arrays)):
            if arrays[j][-1] > largest1 and small_index1 != j:
                largest1 = arrays[j][-1]
                large_index1 = j
            
        print(f" largest1 : {largest1 }")

        diff1 = largest1 - smallest1


        for j in range(len(arrays)):
            if arrays[j][-1] > largest2:
                largest2 = arrays[j][-1]
                large_index2 = j
        
        

        for i in range(len(arrays)):
            if arrays[i][0] < smallest2 and large_index2 != i:
                smallest2 = arrays[i][0]
                small_index2 = i

        print(f"largest2 : {largest2} smallest2: {smallest2}")

        diff2 = largest2 - smallest2

        # print(f"largest : {largest}")
        return abs(max(diff1, diff2))
                        