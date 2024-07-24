class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.buildTree(nums, 0, 0, self.n - 1)

    def buildTree(self, nums, tree_index, low, high):
        if low == high:
            self.tree[tree_index] = nums[low]
            return

        mid = (low + high) // 2
        self.buildTree(nums, 2 * tree_index + 1, low, mid)
        self.buildTree(nums, 2 * tree_index + 2, mid + 1, high)
        self.tree[tree_index] = (
            self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]
        )

    def updateTree(self, tree_index, low, high, idx, val):
        if low == high:
            self.tree[tree_index] = val
            return

        mid = (low + high) // 2
        if idx <= mid:
            self.updateTree(2 * tree_index + 1, low, mid, idx, val)
        else:
            self.updateTree(2 * tree_index + 2, mid + 1, high, idx, val)
        self.tree[tree_index] = (
            self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]
        )

    def queryTree(self, tree_index, low, high, i, j):
        if low > j or high < i:
            return 0

        if i <= low and j >= high:
            return self.tree[tree_index]

        mid = (low + high) // 2
        if i > mid:
            return self.queryTree(2 * tree_index + 2, mid + 1, high, i, j)
        elif j <= mid:
            return self.queryTree(2 * tree_index + 1, low, mid, i, j)
        else:
            return self.queryTree(
                2 * tree_index + 1, low, mid, i, mid
            ) + self.queryTree(2 * tree_index + 2, mid + 1, high, mid + 1, j)

    def update(self, index: int, val: int) -> None:
        self.updateTree(0, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.queryTree(0, 0, self.n - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
