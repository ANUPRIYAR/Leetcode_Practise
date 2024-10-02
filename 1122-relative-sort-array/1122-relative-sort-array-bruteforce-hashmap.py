class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freqmap = dict()

        for num in arr1:
            freqmap[num] = freqmap.get(num, 0) + 1

        res = []
        for num in arr2:
            for i in range(freqmap[num]):
                res.append(num)

            del freqmap[num]
        freqmap = dict(sorted(freqmap.items(), key= lambda x: x[0]))
        for key, value in freqmap.items():
            for i in range(value):
                res.append(key)

        return res

        