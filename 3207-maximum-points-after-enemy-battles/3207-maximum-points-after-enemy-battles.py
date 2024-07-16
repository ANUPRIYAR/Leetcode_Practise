class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        start, end = 0, len(enemyEnergies) - 1
        # points = 0
        print(enemyEnergies[start])
        points = currentEnergy// enemyEnergies[start]
        currentEnergy = currentEnergy % enemyEnergies[start]
        
        while start <= end:
            if currentEnergy >= enemyEnergies[start]:
                # currentEnergy -= enemyEnergies[start]
                # if currentEnergy // enemyEnergies[start] >= 1
                points += currentEnergy// enemyEnergies[start]
                currentEnergy = currentEnergy % enemyEnergies[start]
                print(currentEnergy)
                # points += 1
            elif points > 0 and currentEnergy < enemyEnergies[start]:
                currentEnergy += enemyEnergies[end]
                end -= 1
            else:
                return 0
            
        return points