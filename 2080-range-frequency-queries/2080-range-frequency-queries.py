

class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.arr = arr
        # self.tree = [0] * (4* self.n )
        self.tree =[None]* (4*self.n)
        self.buildTree( 0, 0, self.n -1)

    def buildTree(self,  idx, start, end):
        # leaf node
        if start == end:
            self.tree[idx] ={self.arr[start]: 1}
        else:

            mid = (start + end)//2
            left_child = 2*idx + 1
            right_child = 2*idx +2
            self.buildTree( left_child, start, mid)
            self.buildTree(right_child, mid + 1, end)
            # self.tree[idx] = self.tree[2*idx + 1] + self.tree[2*idx + 2] 
            self.tree[idx] = self.merge(self.tree[left_child], self.tree[right_child])


    def merge(self, left_dict, right_dict):
        merged = {}
        for key in left_dict:
            merged[key] = merged.get(key, 0) + left_dict[key]

        for key in right_dict:
            merged[key] = merged.get(key, 0) + right_dict[key]

        return merged


    def queryfreq(self, arr, idx, start, end, l, r, key):
        if r < start or l > end:
            return 0

        if l <= start and r >= end:
            return self.tree[idx].get(key, 0)

        mid = (start + end)//2
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2

        left_freq = self.queryfreq(arr, left_child, start, mid, l, r, key)
        right_freq = self.queryfreq(arr, right_child, mid + 1, end, l, r, key)
        return left_freq + right_freq

        # if l > mid:
        #     queryfreq(arr, 2*idx + 2, mid + 1, end, l, r, key )
        # elif r <= mid:
        #     queryfreq(arr, 2*idx + 1, start, mid, l, r, key)
        # else:
        #     return self.queryrange(arr, 2*idx + 1, start, mid, l, r) + self.queryrange(arr, 2*idx + 2, mid + 1, end, l, r )

        

    def query(self, left: int, right: int, value: int) -> int:
        return self.queryfreq( self.arr, 0, 0, self.n -1 , left, right, value)
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)