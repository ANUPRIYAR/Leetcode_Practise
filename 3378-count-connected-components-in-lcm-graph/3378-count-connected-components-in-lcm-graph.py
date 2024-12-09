class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        
        def find(u):
            if u not in root:
                root[u] = u
            if root[u] != u:
                root[u] = find(root[u])
            return root[u]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u == root_v:
                return 
            if rank[root_u] < rank[root_v]:
                root[root_u] = root_v
            else:
                root[root_v] = root_u
                rank[root_u] += rank[root_v]

        nums.sort()
        if nums[0] == 1:
            cuttoff = bisect.bisect_left(nums, threshold + 1)
            return len(nums) - cuttoff + 1

        root = {}
        rank = defaultdict(lambda: 1)

        for i, num in enumerate(nums):
            if num in root:
                continue

            find(num)
            for multiple in range(num + num, threshold + 1, num):
                union(num, multiple)

        for u in root:
            find(u)

        return len(set(root.values()))




                



        
        