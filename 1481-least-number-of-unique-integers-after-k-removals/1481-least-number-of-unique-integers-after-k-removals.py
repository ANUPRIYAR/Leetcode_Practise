class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        n = len(arr)
        elemfreq = dict()
        for num in arr:
            elemfreq[num] = elemfreq.get(num, 0) + 1

        freqcount = [0]* (n + 1)
        for key, value in elemfreq.items():
            freqcount[value] += 1

        # print(freqcount)

        uniqueelems = len(elemfreq)

        for i in range(1, n + 1):
            elementsToRemove = min(k//i, freqcount[i])
            k -= i * elementsToRemove
            uniqueelems -= elementsToRemove
            if k < i:
                return uniqueelems

        return 0
        