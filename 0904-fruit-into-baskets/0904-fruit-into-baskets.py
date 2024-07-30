class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 0
        maxfruits = 0
        hashmap = dict()
        n = len(fruits)

        while end < n:
            fruit = fruits[end]
            hashmap[fruit] = hashmap.get(fruit, 0) + 1

            while (len(hashmap)) > 2:
                first_fruit = fruits[start]
                hashmap[first_fruit] -= 1
                if hashmap[first_fruit] == 0:
                    del hashmap[first_fruit]

                start += 1


            maxfruits = max(maxfruits, end - start + 1)
            end += 1

        return maxfruits


        