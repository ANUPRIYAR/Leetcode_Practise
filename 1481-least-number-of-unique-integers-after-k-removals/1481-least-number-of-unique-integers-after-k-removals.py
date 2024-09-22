class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = dict()

        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1

        hashmap = dict(sorted(hashmap.items(), key = lambda x:x [1]))

        n = len(hashmap)
        for key in hashmap:
            if hashmap[key] <= k:
                k -= hashmap[key]
                n -= 1
        return n
            
            # hashmap[key] -= 1
            # if hashmap[key] == 0:
            #     del hashmap[key]
            # if remove == k:
            #     return 

            


