class Solution:
    def update(self, node, start, end, pos, val, tree):
        if start == end:
            tree[node] += val
        else:
            mid = (start + end)//2
            if start <= pos <= mid:
                self.update(node*2 + 1, start, mid, pos, val, tree)
            else:
                self.update(2*node + 2, mid + 1, end, pos, val, tree)
            tree[node] = tree[2*node + 1] + tree[2*node + 2]

    def query(self, node, start, end, l, r, tree):
        if l > end or r < start:
            return 0

        if l <= start and r >= end:
            return tree[node]

        mid = start + (end - start)//2
        left = self.query(node*2 + 1, start, mid, l, r, tree)
        right = self.query(2*node + 2, mid + 1, end, l, r, tree)
        return left + right

    def numTeams(self, rating: List[int]) -> int:
        teamcount = 0
        maxratings = max(rating) + 1
        lefttree = [0]* (4* maxratings)
        righttree = [0]* (4* maxratings)

        for i in range(1, len(rating)):
            self.update(0, 0, maxratings - 1, rating[i], 1, righttree)
        self.update(0, 0, maxratings - 1, rating[0], 1, lefttree)

        for i in range(1, len(rating)):
            leftlesscount = self.query(0, 0, maxratings - 1, 0, rating[i] - 1, lefttree )
            rightgreatercount = self.query(0, 0, maxratings - 1, rating[i] + 1, maxratings - 1, righttree )
            teamcount += leftlesscount * rightgreatercount 

            leftgreatercount = self.query(0, 0, maxratings - 1, rating[i] + 1, maxratings - 1, lefttree)
            rightlesscount = self.query(0, 0, maxratings - 1, 0, rating[i] - 1, righttree)
            teamcount += leftgreatercount * rightlesscount

            self.update(0,0, maxratings - 1,rating[i], 1, lefttree )
            self.update(0,0, maxratings - 1, rating[i], -1, righttree )

        return teamcount

        