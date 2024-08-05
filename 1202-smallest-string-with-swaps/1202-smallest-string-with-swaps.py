class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = {}
        n = len(s)
        def find(u):
            if u not in uf:
                uf[u] = u
            if uf[u] != u:
                uf[u] = find(uf[u])

            return uf[u]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            uf[root_x]= root_y


        for x, y in pairs:
            union(x, y)

        char_group = defaultdict(list)
        for i,c in enumerate(s):
            char_group[find(i)].append(c)
        # print(char_group)

        # Sort characters in each group in descending order to pop smallest char later
        for chars in char_group.values():
            chars.sort(reverse=True)
        # print(char_group)
        
      
        # Build the smallest string by popping the smallest available character from the group
        # the current position belongs to
        output = ""
        for i in range(n):
            output += char_group[find(i)].pop()

        return output


        