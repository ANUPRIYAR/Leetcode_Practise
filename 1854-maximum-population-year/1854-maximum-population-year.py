# we subtract 1950 to get smaller index, since from the constraints we know the year given starts from 1950, then 101 => 2051- 1950
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count_map = [0] * 101

     
    # linesweep algorithm where if we are given a range(start and end) we add 1 during its start and minus 1 after its end, here we taking the death year itself since its excluded.
        for log in logs:
            count_map[log[0] - 1950] += 1
            count_map[log[1] - 1950] -= 1
        

        count, max_population = 0, 0
        year = 0

        # taking prefix sum, since we know each person born will be counted until his death year, so when taking prefix sum previous years population is also accounted along with the current year population
        for i in range(101):
            count += count_map[i]    

            # keeping check of max population until the current year
            if count > max_population:
                max_population = count
                year = i  + 1950   

        return year


            


        