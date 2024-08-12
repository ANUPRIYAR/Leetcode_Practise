class Solution:
    def __init__(self):
        self.tree  = []
        self.dp = [] # stores sum of distances of node i to all nodes in its subtree
        self.subtree_size=[] # stores the size of subtree rooted at node i
        result  = [] # stores the sum of distance from node i to all other nodes

    def dfs1(self, node, parent):
        # Initliaze the subtree size
        self.subtree_size[node] = 1

        # Initialize dp[node] as 0 
        self.dp[node] = 0

        for child in self.tree[node]:
            if child == parent:
                continue

            self.dfs1(child, node)

            # Update dp[node] to include the sum of distances in the subtree of the child
            self.dp[node] += self.dp[child] + self.subtree_size[child]

            self.subtree_size[node] += self.subtree_size[child]

    def dfs2(self, node, parent):
        # Initial result for current node
        self.result[node] = self.dp[node]


        for child in self.tree[node]:
            if child == parent:
                continue

            # Save original dp values
            original_dp_node = self.dp[node]
            original_dp_child = self.dp[child]

            # Perform Rerooting
            # Move the root from node to child
            self.dp[node] -= (self.dp[child] + self.subtree_size[child])
            self.dp[child] += self.dp[node] + (len(self.tree) - self.subtree_size[child])

            # Calculate the result for the child node
            self.result[child] = self.dp[child]

            # Recursively reroot tree at the child
            self.dfs2(child, node)

            # Restore orginal dp values
            self.dp[node] = original_dp_node
            self.dp[child] = original_dp_child


    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.tree = [[]for _ in range(n)]
        self.dp = [0]*n
        self.subtree_size = [0]*n
        self.result = [0]*n


        # Build the tree
        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)

        # step 1 : Run the first dfs to compute the values for the root node
        self.dfs1(0, -1)

        # Step 2: Run the second dfs to reroot the tree and compute the result for all nodes 
        self.dfs2(0, -1)

        return self.result


        