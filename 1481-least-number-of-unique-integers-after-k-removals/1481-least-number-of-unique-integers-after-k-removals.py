class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Step 1: Count the frequency of each element
        elementFrequency = Counter(arr)

        n = len(arr)

        # Step 2: Array to count how many elements have a certain frequency
        frequencyCount = [0] * (n + 1)

        # Step 3: Fill the frequencyCount array based on elementFrequency map
        for freq in elementFrequency.values():
            frequencyCount[freq] += 1

        # Total unique elements in the array
        uniqueElements = len(elementFrequency)

        # Step 4: Iterate through possible frequencies and remove elements
        for i in range(1, n + 1):
            # Calculate the number of elements to remove with the current frequency 'i'
            elementsToRemove = min(k // i, frequencyCount[i])

            # Update 'k' by reducing the count of elements we can remove
            k -= i * elementsToRemove
            # Decrease the count of unique elements by the number of elements removed
            uniqueElements -= elementsToRemove

            # If we no longer have enough 'k' to remove another element with the current frequency, return the number of remaining unique elements
            if k < i:
                return uniqueElements

        return 0