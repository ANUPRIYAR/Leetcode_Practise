class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        
        for i in range(n):
            left = (i - 1) % n
            middle = i
            right = (i + 1) % n
            
            if colors[left] != colors[middle] and colors[middle] != colors[right]:
                count += 1
        
        return count