class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = dict()

        for i in range(len(arr)):
            if hashmap.get(2*arr[i], None) is not None:
                if i != hashmap[2*arr[i]]:
                    return True

            if arr[i] % 2 == 0 and hashmap.get(arr[i]//2, None) is not None:
                if i != hashmap[arr[i]//2]:
                    return True

            

            hashmap[arr[i]] = i

        return False
        

        